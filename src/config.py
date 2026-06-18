"""Central project configuration.

The project uses paths relative to the repository root so commands can be run
from the root folder, for example:

    python -m src.data_preprocessing
    python -m src.feature_engineering
    python -m src.train_model
"""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODEL_DIR = PROJECT_ROOT / "flask_app" / "model"

RAW_DATA_1 = RAW_DATA_DIR / "Data1.csv"
RAW_DATA_2 = RAW_DATA_DIR / "Data2.csv"

MERGED_DATA_PATH = PROCESSED_DATA_DIR / "01_merged_customer_data.csv"
CLEANED_DATA_PATH = PROCESSED_DATA_DIR / "02_cleaned_customer_data.csv"
TRAIN_DATA_PATH = PROCESSED_DATA_DIR / "03_train_data.csv"
TEST_DATA_PATH = PROCESSED_DATA_DIR / "03_test_data.csv"

MODEL_PATH = MODEL_DIR / "loan_propensity_model.joblib"
FEATURE_NAMES_PATH = MODEL_DIR / "feature_names.joblib"
THRESHOLD_PATH = MODEL_DIR / "classification_threshold.joblib"

TARGET_COL = "LoanOnCard"
ID_COL = "ID"
ZIP_COL = "ZipCode"

NUMERICAL_COLS = [
    "Age",
    "CustomerSince",
    "HighestSpend",
    "MonthlyAverageSpend",
    "Mortgage",
]

ORDINAL_COLS = [
    "Level",
    "HiddenScore",
]

BINARY_COLS = [
    "Security",
    "FixedDepositAccount",
    "InternetBanking",
    "CreditCard",
]

BASE_MODEL_FEATURES = NUMERICAL_COLS + ORDINAL_COLS + BINARY_COLS

ENGINEERED_FEATURES = [
    "MortgageFlag",
    "RelationshipProductCount",
    "DigitalEngagementFlag",
    "SpendPerCustomerYear",
    "MortgageToHighestSpendRatio",
    "ValueSegmentScore",
]

MODEL_FEATURES = BASE_MODEL_FEATURES + ENGINEERED_FEATURES

RANDOM_STATE = 42
TEST_SIZE = 0.20
DEFAULT_CLASSIFICATION_THRESHOLD = 0.49
