"""FastAPI server exposing endpoints for the example toolkit, with payments endpoint."""
from __future__ import annotations

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from htapy.ingest.cms import read_local_cms_csv
from htapy.transform.canonical import canonicalize_provider_df
from htapy.analytics.indicators import provider_rankings, top_k_providers
from htapy.analytics.payments import aggregate_payments_by_npi
from pathlib import Path
from typing import Optional
import duckdb
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="health-transparency (final)", version="0.3.0")

# Allow local dev React (vite) to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

_duck_conn = duckdb.connect(database=":memory:")
_TABLE_NAME = "canonical_providers"
_PAYMENTS_TABLE = "openpayments_sample"


def _ensure_data_loaded(path: Optional[str] = None) -> None:
    try:
        tables = _duck_conn.execute("SHOW TABLES").fetchall()
    except Exception:
        tables = []
    if any(_TABLE_NAME == row[0] for row in tables):
        return

    if path is None:
        base = Path(__file__).resolve().parents[3]
        path = str(base / "examples" / "data" / "medicare_sample.csv")

    df = read_local_cms_csv(path)
    canonical = canonicalize_provider_df(df)
    _duck_conn.register(_TABLE_NAME, canonical)
    # add a small openpayments sample table for demo (amounts in USD)
    payments = pd.DataFrame([
        {"npi": "1234567890", "company_name": "PharmaCorp", "amount": 5000.0},
        {"npi": "2345678901", "company_name": "MedSupply", "amount": 1200.0},
        {"npi": "3456789012", "company_name": "PharmaCorp", "amount": 300.0},
    ])
    _duck_conn.register(_PAYMENTS_TABLE, payments)


@app.get("/health", tags=["status"])
def health() -> JSONResponse:
    return JSONResponse({"status": "ok", "version": "0.3.0"})


@app.get("/providers", tags=["providers"])
def list_providers(limit: int = Query(100, ge=1, le=1000)) -> JSONResponse:
    _ensure_data_loaded()
    df = _duck_conn.table(_TABLE_NAME).to_df()
    return JSONResponse(df.head(limit).to_dict(orient="records"))


@app.get("/rankings", tags=["analytics"])
def rankings(top: int = Query(10, ge=1, le=100)) -> JSONResponse:
    _ensure_data_loaded()
    df = _duck_conn.table(_TABLE_NAME).to_df()
    ranked = provider_rankings(df)
    return JSONResponse(ranked.head(top).to_dict(orient="records"))


@app.get("/payments/aggregate", tags=["analytics"])
def payments_aggregate() -> JSONResponse:
    _ensure_data_loaded()
    providers = _duck_conn.table(_TABLE_NAME).to_df()
    payments = _duck_conn.table(_PAYMENTS_TABLE).to_df()
    agg = aggregate_payments_by_npi(payments, providers)
    return JSONResponse(agg.to_dict(orient="records"))


@app.get("/provider/{npi}", tags=["providers"])
def provider_detail(npi: str) -> JSONResponse:
    _ensure_data_loaded()
    df = _duck_conn.table(_TABLE_NAME).to_df()
    sub = df[df["npi"] == str(npi)]
    if sub.empty:
        raise HTTPException(status_code=404, detail="provider not found")
    return JSONResponse(sub.to_dict(orient="records"))
