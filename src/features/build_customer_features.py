import pandas as pd
from pathlib import Path

# =====================================================
# PATHS
# =====================================================

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

# =====================================================
# LOAD DATA
# =====================================================

customers = pd.read_csv(
    RAW_PATH / "olist_customers_dataset.csv"
)

orders = pd.read_csv(
    RAW_PATH / "olist_orders_dataset.csv"
)

items = pd.read_csv(
    RAW_PATH / "olist_order_items_dataset.csv"
)

payments = pd.read_csv(
    RAW_PATH / "olist_order_payments_dataset.csv"
)

reviews = pd.read_csv(
    RAW_PATH / "olist_order_reviews_dataset.csv"
)

# =====================================================
# ORDER VALUE FEATURES
# =====================================================

order_value = (
    items.groupby("order_id")
    .agg(
        total_order_value=("price", "sum"),
        total_freight=("freight_value", "sum"),
        total_items=("order_item_id", "count")
    )
    .reset_index()
)

# =====================================================
# PAYMENT FEATURES
# =====================================================

payment_features = (
    payments.groupby("order_id")
    .agg(
        payment_value=("payment_value", "sum"),
        avg_installments=(
            "payment_installments",
            "mean"
        )
    )
    .reset_index()
)

# =====================================================
# REVIEW FEATURES
# =====================================================

review_features = (
    reviews.groupby("order_id")
    .agg(
        review_score=("review_score", "mean")
    )
    .reset_index()
)

# =====================================================
# BUILD ORDER LEVEL TABLE
# =====================================================

order_level = (
    orders
    .merge(order_value, on="order_id", how="left")
    .merge(payment_features, on="order_id", how="left")
    .merge(review_features, on="order_id", how="left")
)

print("\nOrder Level Shape:")
print(order_level.shape)

# =====================================================
# BUILD CUSTOMER LEVEL TABLE
# =====================================================

customer_features = (
    order_level.groupby("customer_id")
    .agg(
        total_orders=("order_id", "count"),
        avg_order_value=("total_order_value", "mean"),
        total_spent=("payment_value", "sum"),
        avg_review_score=("review_score", "mean"),
        avg_installments=("avg_installments", "mean"),
        total_items=("total_items", "sum")
    )
    .reset_index()
)

# =====================================================
# MERGE CUSTOMER INFO
# =====================================================

customer_features = (
    customers
    .merge(
        customer_features,
        on="customer_id",
        how="left"
    )
)

# =====================================================
# SAVE
# =====================================================

output_path = (
    PROCESSED_PATH /
    "customer_features_v1.csv"
)

customer_features.to_csv(
    output_path,
    index=False
)

print("\nCustomer Feature Table Shape:")
print(customer_features.shape)

print("\nSaved To:")
print(output_path)

print("\nFirst 5 Rows:")
print(customer_features.head())