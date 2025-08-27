"""Payments analytics: join OpenPayments to canonical provider data and compute aggregates."""
from __future__ import annotations
import pandas as pd

def aggregate_payments_by_npi(payments_df: pd.DataFrame, providers_df: pd.DataFrame) -> pd.DataFrame:
    """Join payments (with 'npi' column) to providers and aggregate amount per provider."""
    if 'amount' not in payments_df.columns:
        # possible alternative column names
        for c in ('payment_amount', 'amount_usd', 'total_amount'):
            if c in payments_df.columns:
                payments_df = payments_df.rename(columns={c: 'amount'})
                break
    payments_df = payments_df.copy()
    payments_df['npi'] = payments_df['npi'].astype(str).str.strip()
    providers_df = providers_df.copy()
    providers_df['npi'] = providers_df['npi'].astype(str).str.strip()
    merged = payments_df.merge(providers_df[['npi','provider_name','state']], on='npi', how='left')
    agg = merged.groupby(['npi','provider_name','state'], dropna=False).agg(
        total_payments=('amount','sum'), payments_count=('amount','count'), mean_payment=('amount','mean')
    ).reset_index()
    return agg
