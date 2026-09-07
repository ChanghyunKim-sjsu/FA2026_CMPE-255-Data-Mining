"""House Prices workflow preserved for Assignment 1 - Part 1.

The script expects ``data/train.csv`` in the project directory, prints
holdout metrics for the baseline and three regression models, and performs
three-fold cross-validation for Gradient Boosting. The CSV files under
``results/recorded`` are legacy records; this script does not overwrite them.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


RANDOM_STATE = 42
PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_DIR / "data" / "train.csv"


def rmsle(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_pred = np.maximum(y_pred, 0)
    return float(np.sqrt(np.mean((np.log1p(y_pred) - np.log1p(y_true)) ** 2)))


def evaluate_model(name: str, model: Pipeline, x_train, x_valid, y_train, y_valid) -> dict:
    model.fit(x_train, y_train)
    predictions = model.predict(x_valid)
    return {
        "Model": name,
        "RMSE": np.sqrt(mean_squared_error(y_valid, predictions)),
        "MAE": mean_absolute_error(y_valid, predictions),
        "R2": r2_score(y_valid, predictions),
        "RMSLE": rmsle(y_valid.to_numpy(), predictions),
    }


def build_preprocessor(x: pd.DataFrame) -> ColumnTransformer:
    numeric_features = x.select_dtypes(include=["number"]).columns
    categorical_features = x.select_dtypes(exclude=["number"]).columns

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="constant", fill_value="Missing")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features),
        ]
    )


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Missing {DATA_PATH}. Download Kaggle train.csv and place it there before running."
        )

    data = pd.read_csv(DATA_PATH)
    print(f"Loaded data shape: {data.shape}")
    print(f"SalePrice mean: {data['SalePrice'].mean():,.0f}")
    print(f"SalePrice median: {data['SalePrice'].median():,.0f}")
    print(f"SalePrice skewness: {data['SalePrice'].skew():.2f}")

    x = data.drop(columns=["SalePrice", "Id"], errors="ignore")
    y = data["SalePrice"]

    preprocessor = build_preprocessor(x)
    x_train, x_valid, y_train, y_valid = train_test_split(
        x, y, test_size=0.2, random_state=RANDOM_STATE
    )

    baseline_prediction = np.repeat(y_train.median(), len(y_valid))
    baseline = {
        "Model": "Median Baseline",
        "RMSE": np.sqrt(mean_squared_error(y_valid, baseline_prediction)),
        "MAE": mean_absolute_error(y_valid, baseline_prediction),
        "R2": r2_score(y_valid, baseline_prediction),
        "RMSLE": rmsle(y_valid.to_numpy(), baseline_prediction),
    }

    models = [
        baseline,
        evaluate_model(
            "Random Forest",
            Pipeline(
                steps=[
                    ("preprocessor", preprocessor),
                    (
                        "model",
                        RandomForestRegressor(
                            n_estimators=300,
                            random_state=RANDOM_STATE,
                            n_jobs=-1,
                        ),
                    ),
                ]
            ),
            x_train,
            x_valid,
            y_train,
            y_valid,
        ),
        evaluate_model(
            "Gradient Boosting",
            Pipeline(
                steps=[
                    ("preprocessor", preprocessor),
                    (
                        "model",
                        GradientBoostingRegressor(
                            n_estimators=500,
                            learning_rate=0.03,
                            max_depth=3,
                            loss="huber",
                            random_state=RANDOM_STATE,
                        ),
                    ),
                ]
            ),
            x_train,
            x_valid,
            y_train,
            y_valid,
        ),
    ]

    # Log-linear regression uses log1p target transformation manually.
    log_model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", LinearRegression()),
        ]
    )
    log_model.fit(x_train, np.log1p(y_train))
    log_predictions = np.expm1(log_model.predict(x_valid))
    models.insert(
        1,
        {
            "Model": "Log Linear Regression",
            "RMSE": np.sqrt(mean_squared_error(y_valid, log_predictions)),
            "MAE": mean_absolute_error(y_valid, log_predictions),
            "R2": r2_score(y_valid, log_predictions),
            "RMSLE": rmsle(y_valid.to_numpy(), log_predictions),
        },
    )

    print(pd.DataFrame(models))

    gb_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "model",
                GradientBoostingRegressor(
                    n_estimators=500,
                    learning_rate=0.03,
                    max_depth=3,
                    loss="huber",
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )
    folds = KFold(n_splits=3, shuffle=True, random_state=RANDOM_STATE)
    scores = cross_val_score(
        gb_pipeline,
        x,
        y,
        cv=folds,
        scoring="neg_root_mean_squared_log_error",
    )
    print(f"Gradient Boosting 3-fold RMSLE: {-scores.mean():.3f} +/- {scores.std():.3f}")


if __name__ == "__main__":
    main()
