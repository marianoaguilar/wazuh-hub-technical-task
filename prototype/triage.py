"""Mini prototype of the triage ledger (plan workflow/plans/04-prototype.md).

Reads the vulnerability findings exported from the Wazuh indexer, groups them by package
(the action that fixes them), re-applies the decisions stored in the ledger and prints the
"fix first" list: KEV first, then highest EPSS, then CVSS (Phase 3, D8; host importance
left out: the lab has one host).
"""
import argparse
import datetime
import gzip
import json


def group_by_package(findings):
    """One group per package name: the versions, hosts and CVEs it covers."""
    groups = {}
    for f in findings:
        pkg = f["package"]["name"]
        g = groups.setdefault(pkg, {"package": pkg, "versions": set(), "agents": set(),
                                    "cves": set(), "max_cvss": 0.0})
        g["versions"].add(f["package"].get("version", ""))
        g["agents"].add(f["agent"]["id"])
        vuln = f["vulnerability"]
        g["cves"].add(vuln["id"])
        score = (vuln.get("score") or {}).get("base") or 0.0
        g["max_cvss"] = max(g["max_cvss"], float(score))
    return groups


def apply_ledger(groups, ledger, today):
    """Re-apply stored decisions. Returns (open groups, closed groups).

    A decision is reopened if it has expired or if the package version is not the one
    the person decided on.
    """
    decisions = {d["package"]: d for d in ledger}
    open_, closed = {}, {}
    for pkg, g in groups.items():
        d = decisions.get(pkg)
        if d is None:
            open_[pkg] = dict(g, note="new")
        elif datetime.date.fromisoformat(d["expires"]) < today:
            open_[pkg] = dict(g, note="reopened: expired")
        elif g["versions"] != {d["package_version"]}:
            open_[pkg] = dict(g, note="reopened: package changed")
        else:
            closed[pkg] = dict(g, decision=d)
    return open_, closed


def rank(open_groups, kev, epss=None):
    """Fix-first order (D8): groups with a KEV CVE first, then highest EPSS, then highest
    CVSS as a tie-breaker, then name. EPSS is not multiplied by CVSS (FIRST advice)."""
    epss = epss or {}

    def key(g):
        g["kev"] = sorted(g["cves"] & kev)
        g["max_epss"] = max((epss.get(c, 0.0) for c in g["cves"]), default=0.0)
        return (not g["kev"], -g["max_epss"], -g["max_cvss"], g["package"])
    return sorted(open_groups.values(), key=key)


def load_epss(path):
    """Daily FIRST EPSS CSV (gzip): a comment line, then cve,epss,percentile."""
    scores = {}
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith(("#", "cve,")):
                continue
            cve, score, _ = line.rstrip("\n").split(",")
            scores[cve] = float(score)
    return scores


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--findings", default="data/findings.json")
    p.add_argument("--kev", default="data/kev.json")
    p.add_argument("--epss", default="data/epss.csv.gz")
    p.add_argument("--ledger", default="ledger.json")
    p.add_argument("--today", default=datetime.date.today().isoformat())
    p.add_argument("--top", type=int, default=10)
    a = p.parse_args()

    with open(a.findings) as fh:
        findings = [h["_source"] for h in json.load(fh)["hits"]["hits"]]
    with open(a.kev) as fh:
        kev = {v["cveID"] for v in json.load(fh)["vulnerabilities"]}
    try:
        with open(a.ledger) as fh:
            ledger = json.load(fh)["decisions"]
    except FileNotFoundError:
        ledger = []

    groups = group_by_package(findings)
    open_, closed = apply_ledger(groups, ledger, datetime.date.fromisoformat(a.today))
    ranked = rank(open_, kev, load_epss(a.epss))

    print(f"{len(findings)} findings -> {len(groups)} groups (packages): "
          f"{len(closed)} decided, {len(open_)} open, "
          f"{sum(1 for g in ranked if g['kev'])} with a KEV CVE\n")
    print("Decided (re-applied from the ledger):")
    for pkg, g in sorted(closed.items()):
        d = g["decision"]
        print(f"  {pkg}: {d['status']} by {d['owner']} until {d['expires']} - {d['reason']}")
    if not closed:
        print("  (none)")
    print(f"\nFix first (top {a.top}):")
    print(f"  {'#':>2}  {'package':<32} {'CVEs':>4} {'max EPSS':>8} {'max CVSS':>8}  KEV / note")
    for i, g in enumerate(ranked[:a.top], 1):
        flag = ", ".join(g["kev"]) if g["kev"] else "-"
        print(f"  {i:>2}  {g['package']:<32} {len(g['cves']):>4} {g['max_epss']:>8.3f} "
              f"{g['max_cvss']:>8.1f}  {flag} [{g['note']}]")


if __name__ == "__main__":
    main()
