import pandas as pd
import numpy as np

from pathlib import Path

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# ==========================================
# PATHS
# ==========================================

PROCESSED_PATH = Path("data/processed")

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    PROCESSED_PATH /
    "customer_features_v2.csv"
)

print("Original Shape:", df.shape)

# ==========================================
# DROP IDENTIFIERS
# ==========================================

id_cols = [
    "customer_id",
    "customer_unique_id"
]

df_model = df.drop(
    columns=id_cols,
    errors="ignore"
)

# ==========================================
# HANDLE CATEGORICALS
# ==========================================

categorical_cols = [
    "customer_city",
    "customer_state",
    "last_purchase"
]

categorical_cols = [
    col
    for col in categorical_cols
    if col in df_model.columns
]

df_model = df_model.drop(
    columns=categorical_cols,
    errors="ignore"
)

# ==========================================
# MISSING VALUE IMPUTATION
# ==========================================

numeric_cols = (
    df_model
    .select_dtypes(
        include=np.number
    )
    .columns
)

imputer = SimpleImputer(
    strategy="median"
)

df_model[numeric_cols] = (
    imputer.fit_transform(
        df_model[numeric_cols]
    )
)

# ==========================================
# LOG TRANSFORM
# ==========================================

if "monetary_value" in df_model.columns:

    df_model["monetary_value"] = (
        np.log1p(
            df_model["monetary_value"]
        )
    )

# ==========================================
# STANDARD SCALING
# ==========================================

scaler = StandardScaler()

scaled_data = scaler.fit_transform(
    df_model[numeric_cols]
)

df_scaled = pd.DataFrame(
    scaled_data,
    columns=numeric_cols
)

# ==========================================
# SAVE
# ==========================================

output_file = (
    PROCESSED_PATH /
    "customer_features_model_ready.csv"
)

df_scaled.to_csv(
    output_file,
    index=False
)

print(
    "\nSaved:",
    output_file
)

print(
    "\nFinal Shape:",
    df_scaled.shape
)

print(
    "\nPreview:"
)

print(
    df_scaled.head()
)