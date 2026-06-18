"""Unit tests for feature engineering and prediction input contract."""

from __future__ import annotations

import pandas as pd

from src.config import MODEL_FEATURES
from src.feature_engineering import engineer_customer_features


def test_engineer_customer_features_creates_expected_features():
    customer = pd.DataFrame(
        [
            {
                "Age": 45,
                "CustomerSince": 20,
                "HighestSpend": 67,
                "MonthlyAverageSpend": 2.5,
                "Mortgage": 0,
                "Level": 2,
                "HiddenScore": 3,
                "Security": 0,
                "FixedDepositAccount": 1,
                "InternetBanking": 1,
                "CreditCard": 1,
            }
        ]
    )

    engineered = engineer_customer_features(customer)

    for feature in MODEL_FEATURES:
        assert feature in engineered.columns

    assert engineered.loc[0, "RelationshipProductCount"] == 2
    assert engineered.loc[0, "MortgageFlag"] == 0
