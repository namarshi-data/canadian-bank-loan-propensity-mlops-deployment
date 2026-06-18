"""Reusable model evaluation utilities for binary classification."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


def get_positive_class_scores(model, X):
    """Return positive-class scores for ROC-AUC and threshold analysis."""
    if hasattr(model, "predict_proba"):
        return model.predict_proba(X)[:, 1]
    if hasattr(model, "decision_function"):
        return model.decision_function(X)
    raise AttributeError(
        "Model must support predict_proba or decision_function for score-based evaluation."
    )


def predict_with_threshold(scores, threshold: float) -> np.ndarray:
    """Convert model scores into binary predictions using a custom threshold."""
    return (np.asarray(scores) >= threshold).astype(int)


def evaluate_predictions(
    y_true,
    y_pred,
    y_score,
    model_name: str,
    y_train=None,
    y_train_pred=None,
) -> dict:
    """Evaluate predictions using statistical and campaign-oriented metrics."""
    cm = confusion_matrix(y_true, y_pred)
    if cm.shape != (2, 2):
        raise ValueError("This evaluator expects a binary classification problem.")

    tn, fp, fn, tp = cm.ravel()

    metrics = {
        "Model": model_name,
        "Test Accuracy": round(accuracy_score(y_true, y_pred), 4),
        "Precision": round(precision_score(y_true, y_pred, zero_division=0), 4),
        "Recall": round(recall_score(y_true, y_pred, zero_division=0), 4),
        "F1 Score": round(f1_score(y_true, y_pred, zero_division=0), 4),
        "ROC-AUC": round(roc_auc_score(y_true, y_score), 4),
        "False Positives": int(fp),
        "False Negatives": int(fn),
        "True Positives": int(tp),
        "True Negatives": int(tn),
    }

    if y_train is not None and y_train_pred is not None:
        metrics["Train Accuracy"] = round(accuracy_score(y_train, y_train_pred), 4)
        metrics["Train-Test Accuracy Gap"] = round(
            metrics["Train Accuracy"] - metrics["Test Accuracy"],
            4,
        )

    return metrics


def evaluate_classifier(
    model,
    X_train,
    X_test,
    y_train,
    y_test,
    model_name: str,
    threshold: float = 0.50,
) -> dict:
    """Evaluate a fitted classifier using a selected decision threshold."""
    y_train_score = get_positive_class_scores(model, X_train)
    y_test_score = get_positive_class_scores(model, X_test)

    y_train_pred = predict_with_threshold(y_train_score, threshold)
    y_test_pred = predict_with_threshold(y_test_score, threshold)

    return evaluate_predictions(
        y_true=y_test,
        y_pred=y_test_pred,
        y_score=y_test_score,
        model_name=model_name,
        y_train=y_train,
        y_train_pred=y_train_pred,
    )


def find_best_threshold(
    y_true,
    y_score,
    metric: str = "f1",
    thresholds: np.ndarray | None = None,
) -> tuple[float, pd.DataFrame]:
    """Search decision thresholds and return the best threshold with diagnostics."""
    if thresholds is None:
        thresholds = np.round(np.arange(0.05, 0.96, 0.01), 2)

    rows = []
    for threshold in thresholds:
        y_pred = predict_with_threshold(y_score, float(threshold))
        rows.append(
            {
                "threshold": float(threshold),
                "precision": precision_score(y_true, y_pred, zero_division=0),
                "recall": recall_score(y_true, y_pred, zero_division=0),
                "f1": f1_score(y_true, y_pred, zero_division=0),
            }
        )

    threshold_table = pd.DataFrame(rows)
    if metric not in threshold_table.columns:
        raise ValueError(f"Unsupported metric: {metric}")

    best_row = threshold_table.sort_values(metric, ascending=False).iloc[0]
    return float(best_row["threshold"]), threshold_table


def metrics_to_dataframe(metrics: list[dict]) -> pd.DataFrame:
    """Convert model metric dictionaries into a comparison DataFrame."""
    return pd.DataFrame(metrics)


def create_confusion_matrix_table(y_true, y_pred) -> pd.DataFrame:
    """Create a readable confusion matrix table for reporting."""
    cm = confusion_matrix(y_true, y_pred)
    return pd.DataFrame(
        cm,
        index=["Actual No Loan", "Actual Loan"],
        columns=["Predicted No", "Predicted Yes"],
    )
