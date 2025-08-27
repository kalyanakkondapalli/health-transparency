import pytest
from htapy.analytics.payments import aggregate_payments_by_npi

def test_aggregate_payments():
    sample_data = [
        {"npi": "123", "amount": 100},
        {"npi": "123", "amount": 200},
        {"npi": "456", "amount": 50}
    ]
    result = aggregate_payments_by_npi(sample_data)
    assert result["123"]["total"] == 300
    assert result["456"]["total"] == 50
