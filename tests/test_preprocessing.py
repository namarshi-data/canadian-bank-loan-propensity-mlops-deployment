"""Unit tests for preprocessing logic."""

from __future__ import annotations

import pandas as pd

from src.data_preprocessing import clean_customer_data, merge_customer_datasets


def test_merge_customer_datasets_one_to_one():
    data1 = pd.DataFrame(
        {
            "ID": [1, 2],
            "Age": [30, 40],
            "CustomerSince": [5, 10],
            "HighestSpend": [50, 80],
            "ZipCode": [11111, 22222],
            "HiddenScore": [1, 2],
            "MonthlyAverageSpend": [1.5, 2.0],
            "Level": [1, 2],
        }
    )
    data2 = pd.DataFrame(
        {
            "ID": [1, 2],
            "Mortgage": [0, 100],
            "Security": [0, 1],
            "FixedDepositAccount": [0, 0],
            "InternetBanking": [1, 1],
            "CreditCard": [0, 1],
            "LoanOnCard": [0, 1],
        }
    )

    merged = merge_customer_datasets(data1, data2)

    assert merged.shape == (2, 14)
    assert merged["ID"].tolist() == [1, 2]


def test_clean_customer_data_corrects_negative_customersince():
    data = pd.DataFrame(
        {
            "ID": [1],
            "Age": [24],
            "CustomerSince": [-2],
            "HighestSpend": [20],
            "ZipCode": [11111],
            "HiddenScore": [1],
            "MonthlyAverageSpend": [1.0],
            "Level": [1],
            "Mortgage": [0],
            "Security": [0],
            "FixedDepositAccount": [0],
            "InternetBanking": [1],
            "CreditCard": [0],
            "LoanOnCard": [0],
        }
    )

    cleaned = clean_customer_data(data)

    assert cleaned.loc[0, "CustomerSince"] == 0
    assert cleaned.loc[0, "LoanOnCard"] == 0
