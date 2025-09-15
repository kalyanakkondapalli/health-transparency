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

## Statement of Need

Healthcare spending and provider transparency data are often fragmented across multiple federal and state sources (CMS, OpenPayments, openFDA). While these datasets are public, they are difficult to use reproducibly due to issues with pagination, caching, schema variation, and lack of standardized analytics workflows.

Researchers, educators, and policymakers need accessible tools that simplify data ingestion, cleaning, and analysis while ensuring reproducibility. Existing packages either focus narrowly on a single dataset or do not provide an integrated pipeline for analysis, API exposure, and visualization.

- health-transparency addresses this gap by providing:

- Modular ingestion connectors with caching and pagination.

- Analytics primitives to link payments with providers and compute metrics.

- A FastAPI server exposing healthcare transparency endpoints.

- A React dashboard scaffold for rapid exploration.

This enables public health researchers, educators, and students to build reproducible workflows and dashboards for healthcare transparency without reinventing ingestion and analytics pipelines.

## Reproducibility

Run tests with `pytest` and start the API as documented in README.

## References

- FastAPI: https://fastapi.tiangolo.com/
- requests-cache: https://requests-cache.readthedocs.io/
- CMS Data: https://data.cms.gov/
- openFDA: https://open.fda.gov/
