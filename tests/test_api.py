import pytest
from fastapi.testclient import TestClient
from htapy.api.server import app
from unittest.mock import patch

client = TestClient(app)

@patch("htapy.analytics.payments.aggregate_payments_by_npi")
def test_payments_endpoint(mock_agg):
    mock_agg.return_value = {"123": {"total": 300}}
    response = client.get("/payments/aggregate")
    assert response.status_code == 200
    assert response.json()["123"]["total"] == 300
