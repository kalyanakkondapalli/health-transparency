"""Tests for HTTP connectors using responses to mock endpoints.""" 
import responses
from htapy.ingest.cms_api import fetch_socrata_csv
import json

@responses.activate
def test_fetch_socrata_csv_json():
    url = 'https://example.com/data.json'
    # Simulate two pages
    page1 = [{"npi":"1","provider_name":"A"}]
    page2 = [{"npi":"2","provider_name":"B"}]
    responses.add(responses.GET, url, json=page1, status=200)
    responses.add(responses.GET, url, json=page2, status=200)
    dfs = list(fetch_socrata_csv(url, params=None, page_size=1))
    assert len(dfs) == 2
    assert dfs[0].iloc[0]['npi'] == '1'
