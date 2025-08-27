"""CMS HTTP connector (generic Socrata-like) with pagination and caching.

This connector is generic: users must provide the dataset endpoint slug or full URL.
It supports Socrata-style `$limit`/`$offset` pagination and simple caching via requests-cache.
"""
from __future__ import annotations
import requests
from typing import Optional, Dict, Iterator
import pandas as pd
import requests_cache

DEFAULT_PAGE_SIZE = 1000

def create_session(cache_name: Optional[str] = None, expire_after: int = 300):
    if cache_name:
        session = requests_cache.CachedSession(cache_name, expire_after=expire_after)
    else:
        session = requests.Session()
    return session

def fetch_socrata_csv(endpoint: str, params: Optional[Dict] = None, session: Optional[requests.Session] = None, page_size: int = DEFAULT_PAGE_SIZE) -> Iterator[pd.DataFrame]:
    """Fetch rows from a Socrata JSON/CSV endpoint using limit/offset pagination.

    Yields pandas DataFrames per page.
    """
    if session is None:
        session = create_session()
    params = dict(params or {})
    offset = 0
    while True:
        params.update({"$limit": page_size, "$offset": offset})
        r = session.get(endpoint, params=params, timeout=30)
        r.raise_for_status()
        # Attempt to parse as JSON first (Socrata returns JSON by default)
        try:
            data = r.json()
            if not data:
                break
            df = pd.DataFrame(data)
        except ValueError:
            # fall back to CSV
            from io import StringIO
            df = pd.read_csv(StringIO(r.text))
            if df.empty:
                break
        yield df
        if len(df) < page_size:
            break
        offset += page_size
