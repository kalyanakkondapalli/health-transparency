# health-transparency

Expanded healthcare transparency & analytics toolkit.

[![CI](https://img.shields.io/github/actions/workflow/status/yourusername/health-transparency/ci.yml?branch=main)](https://github.com/yourusername/health-transparency/actions)
[![PyPI version](https://img.shields.io/pypi/v/health-transparency)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)]()
[![DOI](https://zenodo.org/badge/1045697101.svg)](https://doi.org/10.5281/zenodo.16967350)

## Summary:
  health-transparency is an open-source toolkit for healthcare transparency and analytics. It provides reproducible pipelines to ingest, transform, and analyze healthcare datasets, including CMS, OpenPayments, and openFDA data. The package includes a FastAPI server to expose analytics endpoints, a scaffold React dashboard for visual exploration, and unit tests to ensure correctness.

## Highlights:

- Modular Python package with connectors, analytics, and API.

- Supports caching and paginated ingestion for large datasets.

- Designed for extensibility and community contributions.

## Intended Use:

- Research and analysis of healthcare spending and provider transparency.

- Educational purposes for students and public health practitioners.

- Base framework for building dashboards, reports, and analytics pipelines.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .[dev]
uvicorn htapy.api.server:app --reload
```
See `RELEASE_NOTES.md` and `zenodo_metadata.json` for the exact metadata to use.


## 🔮 Future Work & Suggestions
This project provides a core framework for healthcare transparency and analytics. Future improvements could include:

- **Data Sources**
  - Expanded CMS datasets (hospital compare, provider utilization, Medicare spending).
  - Integration with state-level transparency APIs.
  - Better caching and offline data bundles.

- **Analytics**
  - Fairness metrics (equity of spending, demographic comparisons).
  - Geospatial mapping of providers and payments.
  - Time-series analysis of trends over years.

- **API & Infrastructure**
  - Rate-limiting and authentication for multi-user deployments.
  - Full Docker Compose stack with Postgres for persistent storage.
  - Cloud deployment templates (AWS/GCP/Azure).

- **User Interfaces**
  - Full React/Next.js dashboard with charts and filtering.
  - Jupyter notebook tutorials with reproducible analyses.
  - R bindings for cross-discipline adoption.

- **Community**
  - Open governance model and contribution guidelines.
  - Example research questions for public health students.
  - Datasets curated for teaching purposes.
