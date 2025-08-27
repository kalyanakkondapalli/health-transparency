import pytest
from unittest.mock import patch
from htapy.ingest import cms_api, openpayments_api

@patch("htapy.ingest.cms_api.httpx.get")
def test_cms_fetch(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"provider": "A", "payment": 100}]
    data = cms_api.fetch_cms_data()
    assert data[0]["payment"] == 100

@patch("htapy.ingest.openpayments_api.httpx.get")
def test_openpayments_fetch(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"npi": "12345", "amount": 200}]
    data = openpayments_api.fetch_openpayments_data()
    assert data[0]["amount"] == 200
