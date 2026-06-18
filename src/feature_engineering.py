"""Feature engineering and train-test split utilities.

The feature set is intentionally explainable for a banking marketing use case:
customer tenure, spending behaviour, product relationship indicators, digital
engagement, and mortgage exposure.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import (
    BASE_MODEL_FEATURES,
    CLEANED_DATA_PATH,
    ID_COL,
    MODEL_FEATURES,
    RANDOM_STATE,
    TARGET_COL,
    TEST_DATA_PATH,
    TEST_SIZE,
    TRAIN_DATA_PATH,
    ZIP_COL,
)
from src.utils import ensure_directory


def load_cleaned_data(file_path: str | Path = CLEANED_DATA_PATH) -> pd.DataFrame:
    """Load cleaned customer data created by data_preprocessing."""
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {file_path}. "
            "Run python -m src.data_preprocessing first."
        )
    return pd.read_csv(file_path)


def engineer_customer_features(data: pd.DataFrame) -> pd.DataFrame:
    """Create explainable customer-level features used for modeling and scoring."""
    engineered_data = data.copy()

    missing_base_features = [
        column for column in BASE_MODEL_FEATURES if column not in engineered_data.columns
    ]
    if missing_base_features:
        raise ValueError(f"Missing base features: {missing_base_features}")

    engineered_data["CustomerSince"] = engineered_data["CustomerSince"].clip(lower=0)

    engineered_data["MortgageFlag"] = (engineered_data["Mortgage"] > 0).astype(int)
    engineered_data["RelationshipProductCount"] = engineered_data[
        ["Security", "FixedDepositAccount", "CreditCard"]
    ].sum(axis=1)
    engineered_data["DigitalEngagementFlag"] = engineered_data["InternetBanking"].astype(int)
    engineered_data["SpendPerCustomerYear"] = (
        engineered_data["MonthlyAverageSpend"] / (engineered_data["CustomerSince"] + 1)
    )
    engineered_data["MortgageToHighestSpendRatio"] = (
        engineered_data["Mortgage"] / (engineered_data["HighestSpend"] + 1)
    )
    engineered_data["ValueSegmentScore"] = (
        engineered_data["Level"]
        + engineered_data["FixedDepositAccount"]
        + (engineered_data["MonthlyAverageSpend"] >= engineered_data["MonthlyAverageSpend"].median()).astype(int)
    )

    return engineered_data


def prepare_modeling_dataset(
    data: pd.DataFrame,
    drop_identifier: bool = True,
    drop_zipcode: bool = True,
) -> pd.DataFrame:
    """Prepare cleaned customer data for supervised model training."""
    modeling_data = engineer_customer_features(data)

    columns_to_drop: list[str] = []
    if drop_identifier and ID_COL in modeling_data.columns:
        columns_to_drop.append(ID_COL)
    if drop_zipcode and ZIP_COL in modeling_data.columns:
        columns_to_drop.append(ZIP_COL)
    if columns_to_drop:
        modeling_data = modeling_data.drop(columns=columns_to_drop)

    if TARGET_COL not in modeling_data.columns:
        raise ValueError(f"Target column not found: {TARGET_COL}")

    missing_features = [
        column for column in MODEL_FEATURES if column not in modeling_data.columns
    ]
    if missing_features:
        raise ValueError(f"Missing modeling features: {missing_features}")

    modeling_data[TARGET_COL] = modeling_data[TARGET_COL].astype(int)
    return modeling_data[MODEL_FEATURES + [TARGET_COL]].copy()


def split_features_target(
    data: pd.DataFrame,
    target_col: str = TARGET_COL,
) -> tuple[pd.DataFrame, pd.Series]:
    """Separate predictors and target variable."""
    if target_col not in data.columns:
        raise ValueError(f"Target column not found: {target_col}")
    X = data.drop(columns=[target_col]).copy()
    y = data[target_col].copy()
    return X, y


def create_train_test_split(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Create a stratified train-test split for imbalanced classification."""
    return train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state,
    )


def save_train_test_data(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    train_path: str | Path = TRAIN_DATA_PATH,
    test_path: str | Path = TEST_DATA_PATH,
    target_col: str = TARGET_COL,
) -> None:
    """Save prepared train and test datasets."""
    train_data = X_train.copy()
    train_data[target_col] = y_train.values

    test_data = X_test.copy()
    test_data[target_col] = y_test.values

    train_path = Path(train_path)
    test_path = Path(test_path)
    ensure_directory(train_path.parent)
    ensure_directory(test_path.parent)

    train_data.to_csv(train_path, index=False)
    test_data.to_csv(test_path, index=False)


def run_feature_engineering(
    cleaned_data_path: str | Path = CLEANED_DATA_PATH,
    train_output_path: str | Path = TRAIN_DATA_PATH,
    test_output_path: str | Path = TEST_DATA_PATH,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Run feature engineering and save train-test datasets."""
    data = load_cleaned_data(cleaned_data_path)
    modeling_data = prepare_modeling_dataset(data)
    X, y = split_features_target(modeling_data)
    X_train, X_test, y_train, y_test = create_train_test_split(X, y)

    save_train_test_data(
        X_train,
        X_test,
        y_train,
        y_test,
        train_output_path,
        test_output_path,
    )
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = run_feature_engineering()
    print(f"Training data shape: {X_train.shape}")
    print(f"Testing data shape : {X_test.shape}")
