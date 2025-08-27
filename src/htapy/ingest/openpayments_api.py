"""OpenPayments connector: fetch OpenPayments CSV via CMS or API endpoints.

This module provides helpers to stream CSV results with pagination.
"""
from __future__ import annotations
from typing import Optional, Iterator, Dict
import pandas as pd
import requests
import requests_cache

def fetch_openpayments_csv(url: str, params: Optional[Dict] = None, session: Optional[requests.Session] = None, chunk_size: int = 1000) -> Iterator[pd.DataFrame]:
    if session is None:
        session = requests.Session()
    params = dict(params or {})
    offset = 0
    while True:
        params.update({"$limit": chunk_size, "$offset": offset})
        r = session.get(url, params=params, timeout=60)
        r.raise_for_status()
        try:
            data = r.json()
            if not data:
                break
            df = pd.DataFrame(data)
        except ValueError:
            from io import StringIO
            df = pd.read_csv(StringIO(r.text))
            if df.empty:
                break
        yield df
        if len(df) < chunk_size:
            break
        offset += chunk_size
