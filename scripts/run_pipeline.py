"""Run the full local ML pipeline from raw data to trained model artifacts."""

from __future__ import annotations

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data_preprocessing import run_data_preprocessing
from src.feature_engineering import run_feature_engineering
from src.train_model import train_final_model


def main() -> None:
    """Execute the project pipeline in the correct order."""
    print("1/3 Data cleaning and preprocessing")
    cleaned_data = run_data_preprocessing()
    print(f"   Cleaned data shape: {cleaned_data.shape}")

    print("2/3 Feature engineering and train-test split")
    X_train, X_test, y_train, y_test = run_feature_engineering()
    print(f"   Train shape: {X_train.shape}; Test shape: {X_test.shape}")

    print("3/3 Model training and artifact export")
    _, metrics, _ = train_final_model(save_model=True)
    print("   Final model metrics:")
    for key, value in metrics.items():
        print(f"   - {key}: {value}")


if __name__ == "__main__":
    main()
