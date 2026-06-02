"""Preprocessing utilities for model-ready churn features."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from scipy import sparse
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


TARGET_COLUMN = "Churn"
ID_COLUMN = "customerID"
RANDOM_SEED = 42
TEST_SIZE = 0.2


@dataclass(frozen=True)
class FeatureSplit:
    """Container for train/test features and targets."""

    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series


@dataclass(frozen=True)
class PreprocessedData:
    """Container for fitted preprocessor outputs."""

    X_train_processed: object
    X_test_processed: object
    y_train: pd.Series
    y_test: pd.Series
    preprocessor: ColumnTransformer
    feature_names: list[str]


def create_feature_target_split(
    data: pd.DataFrame,
    target_column: str = TARGET_COLUMN,
    id_column: str = ID_COLUMN,
) -> tuple[pd.DataFrame, pd.Series]:
    """Separate modeling features from the target.

    `customerID` is intentionally excluded from features because it is an
    identifier used for traceability, not a signal that should be learned by a
    model.
    """
    if target_column not in data.columns:
        raise ValueError(f"Missing target column: {target_column}")

    columns_to_drop = [target_column]
    if id_column in data.columns:
        columns_to_drop.append(id_column)

    X = data.drop(columns=columns_to_drop)
    y = data[target_column]

    if target_column in X.columns:
        raise ValueError(f"Target column leaked into features: {target_column}")
    if id_column in X.columns:
        raise ValueError(f"ID column leaked into features: {id_column}")

    return X, y


def create_train_test_split(
    data: pd.DataFrame,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_SEED,
) -> FeatureSplit:
    """Create a reproducible stratified train/test split."""
    X, y = create_feature_target_split(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    return FeatureSplit(
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
    )


def get_feature_columns(data: pd.DataFrame) -> tuple[list[str], list[str]]:
    """Identify numeric and categorical columns for preprocessing."""
    numeric_columns = data.select_dtypes(include=["number", "bool"]).columns.tolist()
    categorical_columns = data.select_dtypes(
        include=["object", "string", "category"]
    ).columns.tolist()
    return numeric_columns, categorical_columns


def build_preprocessing_pipeline(data: pd.DataFrame) -> ColumnTransformer:
    """Build the sklearn preprocessing pipeline for the feature matrix."""
    numeric_columns, categorical_columns = get_feature_columns(data)

    numeric_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_columns),
            ("categorical", categorical_pipeline, categorical_columns),
        ],
        remainder="drop",
    )


def fit_transform_train_test(split: FeatureSplit) -> PreprocessedData:
    """Fit preprocessing on train data and transform train/test separately."""
    preprocessor = build_preprocessing_pipeline(split.X_train)
    X_train_processed = preprocessor.fit_transform(split.X_train)
    X_test_processed = preprocessor.transform(split.X_test)
    feature_names = preprocessor.get_feature_names_out().tolist()

    return PreprocessedData(
        X_train_processed=X_train_processed,
        X_test_processed=X_test_processed,
        y_train=split.y_train,
        y_test=split.y_test,
        preprocessor=preprocessor,
        feature_names=feature_names,
    )


def get_matrix_shape(matrix: object) -> tuple[int, int]:
    """Return the shape of dense or sparse feature matrices."""
    if sparse.issparse(matrix):
        return matrix.shape
    return matrix.shape
