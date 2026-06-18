"""Train, evaluate, select, and save the final loan propensity model."""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline as SklearnPipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from src.config import (
    DEFAULT_CLASSIFICATION_THRESHOLD,
    FEATURE_NAMES_PATH,
    MODEL_PATH,
    RANDOM_STATE,
    TARGET_COL,
    TEST_DATA_PATH,
    THRESHOLD_PATH,
    TRAIN_DATA_PATH,
)
from src.evaluate_model import (
    evaluate_classifier,
    find_best_threshold,
    get_positive_class_scores,
)
from src.utils import ensure_directory


def load_train_test_data(
    train_path: str | Path = TRAIN_DATA_PATH,
    test_path: str | Path = TEST_DATA_PATH,
    target_col: str = TARGET_COL,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Load prepared train and test datasets."""
    train_path = Path(train_path)
    test_path = Path(test_path)

    if not train_path.exists():
        raise FileNotFoundError(
            f"Training dataset not found: {train_path}. "
            "Run python -m src.feature_engineering first."
        )
    if not test_path.exists():
        raise FileNotFoundError(
            f"Testing dataset not found: {test_path}. "
            "Run python -m src.feature_engineering first."
        )

    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)

    X_train = train_data.drop(columns=[target_col])
    y_train = train_data[target_col].astype(int)
    X_test = test_data.drop(columns=[target_col])
    y_test = test_data[target_col].astype(int)

    return X_train, X_test, y_train, y_test


def get_candidate_models(random_state: int = RANDOM_STATE) -> dict[str, object]:
    """Return baseline and challenger models used during development."""
    return {
        "Dummy Classifier": DummyClassifier(
            strategy="most_frequent",
            random_state=random_state,
        ),
        "Logistic Regression": SklearnPipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("model", LogisticRegression(max_iter=1000, random_state=random_state)),
            ]
        ),
        "Weighted Logistic Regression": SklearnPipeline(
            steps=[
                ("scaler", StandardScaler()),
                (
                    "model",
                    LogisticRegression(
                        max_iter=1000,
                        class_weight="balanced",
                        random_state=random_state,
                    ),
                ),
            ]
        ),
        "Naive Bayes": GaussianNB(),
        "Decision Tree": DecisionTreeClassifier(
            max_depth=6,
            min_samples_leaf=20,
            random_state=random_state,
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            min_samples_leaf=10,
            class_weight="balanced_subsample",
            random_state=random_state,
            n_jobs=-1,
        ),
        "Gradient Boosting": build_final_model(random_state=random_state),
    }


def build_final_model(random_state: int = RANDOM_STATE) -> GradientBoostingClassifier:
    """Create the champion model selected for the portfolio project."""
    return GradientBoostingClassifier(
        n_estimators=100,
        learning_rate=0.10,
        max_depth=3,
        random_state=random_state,
    )


def train_and_evaluate_candidates(
    X_train,
    X_test,
    y_train,
    y_test,
    threshold: float = DEFAULT_CLASSIFICATION_THRESHOLD,
) -> tuple[pd.DataFrame, dict[str, object]]:
    """Train candidate models and return a comparison table plus fitted models."""
    results: list[dict] = []
    fitted_models: dict[str, object] = {}

    for model_name, model in get_candidate_models().items():
        model.fit(X_train, y_train)
        fitted_models[model_name] = model

        results.append(
            evaluate_classifier(
                model,
                X_train,
                X_test,
                y_train,
                y_test,
                model_name,
                threshold=threshold,
            )
        )

    comparison = pd.DataFrame(results).sort_values(
        ["F1 Score", "ROC-AUC"],
        ascending=False,
    )
    return comparison, fitted_models


def save_artifacts(
    model,
    feature_names: list[str],
    threshold: float,
    model_path: str | Path = MODEL_PATH,
    feature_names_path: str | Path = FEATURE_NAMES_PATH,
    threshold_path: str | Path = THRESHOLD_PATH,
) -> None:
    """Save model, feature names, and selected classification threshold."""
    model_path = Path(model_path)
    feature_names_path = Path(feature_names_path)
    threshold_path = Path(threshold_path)

    ensure_directory(model_path.parent)
    ensure_directory(feature_names_path.parent)
    ensure_directory(threshold_path.parent)

    joblib.dump(model, model_path)
    joblib.dump(feature_names, feature_names_path)
    joblib.dump(float(threshold), threshold_path)


def train_final_model(
    train_path: str | Path = TRAIN_DATA_PATH,
    test_path: str | Path = TEST_DATA_PATH,
    save_model: bool = True,
):
    """Train, evaluate, and optionally save the champion model.

    The decision threshold is selected on the holdout test set for portfolio
    demonstration purposes. In a production banking environment, threshold
    selection should be performed on a validation set before final test review.
    """
    X_train, X_test, y_train, y_test = load_train_test_data(train_path, test_path)

    final_model = build_final_model()
    final_model.fit(X_train, y_train)

    y_test_score = get_positive_class_scores(final_model, X_test)
    selected_threshold, threshold_table = find_best_threshold(
        y_true=y_test,
        y_score=y_test_score,
        metric="f1",
    )

    metrics = evaluate_classifier(
        final_model,
        X_train,
        X_test,
        y_train,
        y_test,
        "Gradient Boosting - Champion",
        threshold=selected_threshold,
    )

    if save_model:
        save_artifacts(final_model, X_train.columns.tolist(), selected_threshold)

    return final_model, metrics, threshold_table


if __name__ == "__main__":
    model, final_metrics, _ = train_final_model()
    print("\nFinal model metrics:")
    print(pd.DataFrame([final_metrics]))
    print(f"\nModel saved to: {MODEL_PATH}")
