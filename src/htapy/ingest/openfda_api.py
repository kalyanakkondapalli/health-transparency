"""openFDA connector using their public API (limit/skip style)."""
from __future__ import annotations
from typing import Optional, Iterator, Dict
import pandas as pd
import requests

def fetch_openfda(endpoint: str, params: Optional[Dict] = None, session: Optional[requests.Session] = None, limit: int = 100) -> Iterator[pd.DataFrame]:
    if session is None:
        session = requests.Session()
    params = dict(params or {})
    skip = 0
    while True:
        params.update({"limit": limit, "skip": skip})
        r = session.get(endpoint, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        results = data.get("results", [])
        if not results:
            break
        df = pd.DataFrame(results)
        yield df
        if len(results) < limit:
            break
        skip += limit
