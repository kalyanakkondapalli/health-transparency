# health-transparency

Expanded healthcare transparency & analytics toolkit.

[![CI](https://img.shields.io/github/actions/workflow/status/yourusername/health-transparency/ci.yml?branch=main)](https://github.com/yourusername/health-transparency/actions)
[![PyPI version](https://img.shields.io/pypi/v/health-transparency)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)]()
[![DOI](https://zenodo.org/badge/1045697101.svg)](https://doi.org/10.5281/zenodo.16967350)

## Highlights of final changes
- Added **HTTP connectors** for CMS/OpenPayments/openFDA with pagination and optional caching (`requests-cache`).
- Added **payments analytics** to join OpenPayments to provider data and compute payments per provider.
- React dashboard scaffold (`web/`) that calls the API endpoints.
- Coverage reporting and CI workflow (pytest + coverage).
- Zenodo metadata and GitHub release template for DOI minting.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .[dev]
uvicorn htapy.api.server:app --reload
```

## Publishing & DOI (Zenodo)
1. Create a GitHub release `v0.3.0`.
2. Connect GitHub repository to Zenodo and enable DOI for releases.
3. Create the GitHub release — Zenodo will mint a DOI snapshot.

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
