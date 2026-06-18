"""Data loading, merging, cleaning, and validation utilities.

This module is intentionally focused on data quality. It does not train models
and it does not create separate report files. It produces the cleaned data assets
needed by the notebooks and the modeling pipeline.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

from src.config import (
    BINARY_COLS,
    CLEANED_DATA_PATH,
    ID_COL,
    MERGED_DATA_PATH,
    NUMERICAL_COLS,
    ORDINAL_COLS,
    RAW_DATA_1,
    RAW_DATA_2,
    TARGET_COL,
)
from src.utils import ensure_directory


def load_dataset(file_path: str | Path) -> pd.DataFrame:
    """Load a CSV dataset from disk."""
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {file_path}. "
            "Place Data1.csv and Data2.csv in data/raw before running the pipeline."
        )
    return pd.read_csv(file_path)


def validate_required_columns(
    data: pd.DataFrame,
    required_columns: Iterable[str],
    dataset_name: str,
) -> None:
    """Validate that required columns are present."""
    missing_columns = [column for column in required_columns if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns in {dataset_name}: {missing_columns}")


def validate_unique_key(data: pd.DataFrame, key: str, dataset_name: str) -> None:
    """Validate that a key is unique within a dataset."""
    duplicate_count = int(data[key].duplicated().sum())
    if duplicate_count > 0:
        raise ValueError(
            f"{duplicate_count} duplicate values found in {dataset_name}.{key}. "
            "The customer merge expects one row per customer ID."
        )


def merge_customer_datasets(
    data1: pd.DataFrame,
    data2: pd.DataFrame,
    merge_key: str = ID_COL,
) -> pd.DataFrame:
    """Merge the raw customer datasets using a one-to-one customer ID join."""
    validate_required_columns(data1, [merge_key], "Data1")
    validate_required_columns(data2, [merge_key], "Data2")
    validate_unique_key(data1, merge_key, "Data1")
    validate_unique_key(data2, merge_key, "Data2")

    merged_data = pd.merge(
        data1,
        data2,
        on=merge_key,
        how="inner",
        validate="one_to_one",
    )

    expected_rows = min(len(data1), len(data2))
    if len(merged_data) != expected_rows:
        raise ValueError(
            "Merged row count is lower than expected. "
            "Some customer IDs may not match across the raw files."
        )

    return merged_data


def clean_customer_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean the merged customer dataset for analysis and modeling.

    Cleaning decisions:
    - Remove rows with missing target values because they cannot be used for
      supervised model training.
    - Correct negative CustomerSince values to zero. These values represent a
      small data-quality issue and zero is the most conservative correction.
    - Validate binary product flags.
    - Validate duplicate full rows and duplicate customer IDs.
    """
    cleaned_data = data.copy()

    required_columns = [
        TARGET_COL,
        ID_COL,
        *NUMERICAL_COLS,
        *ORDINAL_COLS,
        *BINARY_COLS,
    ]
    validate_required_columns(cleaned_data, required_columns, "merged customer data")

    cleaned_data = cleaned_data.dropna(subset=[TARGET_COL]).copy()
    cleaned_data[TARGET_COL] = cleaned_data[TARGET_COL].astype(int)

    if (cleaned_data["CustomerSince"] < 0).any():
        cleaned_data["CustomerSince"] = cleaned_data["CustomerSince"].clip(lower=0)

    if cleaned_data.duplicated().any():
        raise ValueError("Duplicate full rows found after cleaning.")

    validate_unique_key(cleaned_data, ID_COL, "cleaned customer data")

    for column in BINARY_COLS:
        observed_values = set(cleaned_data[column].dropna().unique())
        invalid_values = observed_values - {0, 1}
        if invalid_values:
            raise ValueError(
                f"Unexpected values in binary column {column}: {invalid_values}"
            )
        cleaned_data[column] = cleaned_data[column].astype("int8")

    for column in ORDINAL_COLS:
        cleaned_data[column] = cleaned_data[column].astype("int8")

    return cleaned_data


def get_data_quality_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Return a compact data quality summary for each column."""
    return pd.DataFrame(
        {
            "feature": data.columns,
            "data_type": data.dtypes.astype(str).values,
            "non_null_count": data.notna().sum().values,
            "missing_count": data.isna().sum().values,
            "missing_pct": (data.isna().mean() * 100).round(2).values,
            "unique_values": data.nunique(dropna=True).values,
        }
    )


def run_data_preprocessing(
    raw_data_1_path: str | Path = RAW_DATA_1,
    raw_data_2_path: str | Path = RAW_DATA_2,
    merged_output_path: str | Path = MERGED_DATA_PATH,
    cleaned_output_path: str | Path = CLEANED_DATA_PATH,
) -> pd.DataFrame:
    """Run the full data preprocessing workflow and save processed outputs."""
    data1 = load_dataset(raw_data_1_path)
    data2 = load_dataset(raw_data_2_path)

    merged_data = merge_customer_datasets(data1, data2)
    merged_output_path = Path(merged_output_path)
    ensure_directory(merged_output_path.parent)
    merged_data.to_csv(merged_output_path, index=False)

    cleaned_data = clean_customer_data(merged_data)
    cleaned_output_path = Path(cleaned_output_path)
    ensure_directory(cleaned_output_path.parent)
    cleaned_data.to_csv(cleaned_output_path, index=False)

    return cleaned_data


if __name__ == "__main__":
    final_data = run_data_preprocessing()
    print(f"Cleaned dataset created with shape: {final_data.shape}")
