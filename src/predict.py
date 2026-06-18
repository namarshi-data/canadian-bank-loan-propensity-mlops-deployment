"""Prediction utilities for customer-level loan propensity scoring."""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd

from src.config import (
    DEFAULT_CLASSIFICATION_THRESHOLD,
    FEATURE_NAMES_PATH,
    MODEL_PATH,
    THRESHOLD_PATH,
)
from src.feature_engineering import engineer_customer_features


def load_artifacts(
    model_path: str | Path = MODEL_PATH,
    feature_names_path: str | Path = FEATURE_NAMES_PATH,
    threshold_path: str | Path = THRESHOLD_PATH,
):
    """Load trained model, feature names, and classification threshold."""
    model_path = Path(model_path)
    feature_names_path = Path(feature_names_path)
    threshold_path = Path(threshold_path)

    if not model_path.exists():
        raise FileNotFoundError(f"Model artifact not found: {model_path}")
    if not feature_names_path.exists():
        raise FileNotFoundError(f"Feature names artifact not found: {feature_names_path}")

    model = joblib.load(model_path)
    feature_names = joblib.load(feature_names_path)
    threshold = (
        joblib.load(threshold_path)
        if threshold_path.exists()
        else DEFAULT_CLASSIFICATION_THRESHOLD
    )
    return model, feature_names, float(threshold)


def prepare_customer_input(
    customer_data: dict | pd.DataFrame,
    feature_names: list[str],
) -> pd.DataFrame:
    """Validate, feature-engineer, and order customer input for prediction."""
    if isinstance(customer_data, dict):
        customer_df = pd.DataFrame([customer_data])
    elif isinstance(customer_data, pd.DataFrame):
        customer_df = customer_data.copy()
    else:
        raise TypeError("customer_data must be a dictionary or pandas DataFrame.")

    customer_features = engineer_customer_features(customer_df)

    missing_features = [
        feature for feature in feature_names if feature not in customer_features.columns
    ]
    if missing_features:
        raise ValueError(f"Missing required features: {missing_features}")

    return customer_features[feature_names].copy()


def classify_probability(probability: float, threshold: float) -> int:
    """Convert a probability score into a binary decision."""
    return int(probability >= threshold)


def predict_customer(
    customer_data: dict | pd.DataFrame,
    model_path: str | Path = MODEL_PATH,
    feature_names_path: str | Path = FEATURE_NAMES_PATH,
    threshold_path: str | Path = THRESHOLD_PATH,
) -> dict:
    """Predict loan propensity for one or more customer records."""
    model, feature_names, threshold = load_artifacts(
        model_path=model_path,
        feature_names_path=feature_names_path,
        threshold_path=threshold_path,
    )
    customer_features = prepare_customer_input(customer_data, feature_names)

    probabilities = model.predict_proba(customer_features)[:, 1]
    predictions = [
        classify_probability(float(probability), threshold)
        for probability in probabilities
    ]

    if len(predictions) == 1:
        prediction = predictions[0]
        probability = round(float(probabilities[0]), 4)
        return {
            "prediction": prediction,
            "loan_acceptance_probability": probability,
            "propensity_label": (
                "High Propensity" if prediction == 1 else "Low Propensity"
            ),
            "classification_threshold": threshold,
        }

    return {
        "predictions": predictions,
        "loan_acceptance_probabilities": [
            round(float(probability), 4) for probability in probabilities
        ],
        "classification_threshold": threshold,
    }


if __name__ == "__main__":
    sample_customer = {
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

    print(predict_customer(sample_customer))
