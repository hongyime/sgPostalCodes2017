## Portability maintenance - 2026-09-27

- Conversion input/output paths are now explicit CLI arguments. Two synthetic mocked-library tests passed on Windows and Linux; no retained data was read or converted.

# STATE — sgPostalCodes2017

**Updated**: 2026-09-16
**Agent**: opencode (Sisyphus-Junior)
**Task**: Baseline wave-2b review

## Status
COMPLETE — baseline review done, no issues found.

## Stack
Python scripts · requests · OneMap SG API (postal codes + MRT/LRT station data)

## Findings
- No AGENTS.md (no standard agent config synced here yet)
- 0 open PRs
- No hardcoded secrets in .py/.js/.html
- Clean working tree on master
- Scripts: download_postal_codes.py, download_postal_codes_nopool.py, extract_lrt_stations.py, extract_mrt_stations.py, jsontocsv.py, mrt_lrt.py
- Previously audited: AUDIT_LOG.md, AUDIT.md, security_audit.md present
- Recent: docs add showcase demo metadata, PR #1 shell/standardise merged

## Next Steps
None. Repo is healthy. Consider syncing AGENTS.md from sourcerepo.
