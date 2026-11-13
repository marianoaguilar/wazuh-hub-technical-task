"""Acceptance tests for the triage ledger prototype (plan workflow/plans/04-prototype.md)."""
import datetime
import unittest

import triage

TODAY = datetime.date(2026, 11, 13)


def finding(pkg, version, cve, cvss, agent="001"):
    return {"agent": {"id": agent},
            "package": {"name": pkg, "version": version},
            "vulnerability": {"id": cve, "severity": "High", "score": {"base": cvss}}}


FINDINGS = [
    finding("openssl", "3.0.2-0ubuntu1.30", "CVE-2026-0001", 7.5),
    finding("openssl", "3.0.2-0ubuntu1.30", "CVE-2026-0002", 5.0),
    finding("curl", "7.81.0-1ubuntu1.20", "CVE-2026-0003", 9.8),
    finding("vim", "2:8.2.3995-1ubuntu2", "CVE-2026-0004", 6.0),
]


def decision(pkg, version, expires="2026-12-31"):
    return {"package": pkg, "package_version": version, "status": "false_positive",
            "reason": "test", "owner": "analyst", "expires": expires}


class TriageTest(unittest.TestCase):
    def setUp(self):
        self.groups = triage.group_by_package(FINDINGS)

    def test_groups_by_package(self):
        self.assertEqual(sorted(self.groups), ["curl", "openssl", "vim"])
        self.assertEqual(self.groups["openssl"]["cves"], {"CVE-2026-0001", "CVE-2026-0002"})
        self.assertEqual(self.groups["openssl"]["max_cvss"], 7.5)

    def test_1_valid_decision_is_reapplied(self):
        ledger = [decision("vim", "2:8.2.3995-1ubuntu2")]
        open_, closed = triage.apply_ledger(self.groups, ledger, TODAY)
        self.assertNotIn("vim", open_)
        self.assertIn("vim", closed)

    def test_2_expired_decision_is_reopened(self):
        ledger = [decision("vim", "2:8.2.3995-1ubuntu2", expires="2026-11-01")]
        open_, closed = triage.apply_ledger(self.groups, ledger, TODAY)
        self.assertIn("vim", open_)
        self.assertEqual(open_["vim"]["note"], "reopened: expired")

    def test_3_package_change_reopens(self):
        ledger = [decision("vim", "2:8.2.3995-1ubuntu1")]
        open_, closed = triage.apply_ledger(self.groups, ledger, TODAY)
        self.assertIn("vim", open_)
        self.assertEqual(open_["vim"]["note"], "reopened: package changed")

    def test_4_kev_ranks_before_higher_cvss(self):
        open_, _ = triage.apply_ledger(self.groups, [], TODAY)
        ranked = triage.rank(open_, kev={"CVE-2026-0002"})
        self.assertEqual([g["package"] for g in ranked], ["openssl", "curl", "vim"])

    def test_5_epss_ranks_before_higher_cvss(self):
        # No KEV: vim (EPSS 0.5, CVSS 6.0) goes before curl (EPSS 0.01, CVSS 9.8).
        open_, _ = triage.apply_ledger(self.groups, [], TODAY)
        epss = {"CVE-2026-0004": 0.5, "CVE-2026-0003": 0.01}
        ranked = triage.rank(open_, kev=set(), epss=epss)
        self.assertEqual([g["package"] for g in ranked], ["vim", "curl", "openssl"])


if __name__ == "__main__":
    unittest.main()
