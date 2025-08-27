---
title: "health-transparency: an open toolkit for healthcare transparency and analytics"
authors:
  - name: Kalyana Krishna Kondapalli
    orcid: 0009-0003-0832-259X
    affiliation: 1
date: 2025-08-27
keywords: [healthcare, transparency, analytics, open-data, reproducibility]
---

## Summary

`health-transparency` provides reproducible pipelines, HTTP connectors (with pagination & caching), analytics primitives, and an API for healthcare transparency. The release includes example fixtures and a React dashboard scaffold.

## Implementation improvements in this release

- **Connectors**: `htapy.ingest.cms_api`, `htapy.ingest.openpayments_api`, `htapy.ingest.openfda_api` — paginated, optionally cached via `requests-cache`.
- **Payments analytics**: `htapy.analytics.payments` joins payments to canonical provider data and computes aggregated metrics.
- **Dashboard**: React scaffold in `/web` demonstrating calls to `/rankings` and `/providers`.
- **Packaging & CI**: `pyproject.toml`, GitHub Actions CI running tests and coverage.
- **Release metadata**: `zenodo_metadata.json` and `RELEASE_NOTES.md` to assist DOI minting.

## Reproducibility

Run tests with `pytest` and start the API as documented in README.

## References

- FastAPI: https://fastapi.tiangolo.com/
- requests-cache: https://requests-cache.readthedocs.io/
- CMS Data: https://data.cms.gov/
- openFDA: https://open.fda.gov/
