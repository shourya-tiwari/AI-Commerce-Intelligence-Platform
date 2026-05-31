import pandas as pd
import numpy as np
from pathlib import Path

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

products = pd.read_csv(
    RAW_PATH / "olist_products_dataset.csv"
)

# =====================================================
# DATE CONVERSION
# =====================================================

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"]
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"]
)

# =====================================================
# CUSTOMER ORDER BASE
# =====================================================

customer_orders = (
    orders.merge(
        customers,
        on="customer_id",
        how="left"
    )
)

# =====================================================
# RFM FEATURES
# =====================================================

reference_date = (
    customer_orders["order_purchase_timestamp"]
    .max()
)

rfm = (
    customer_orders
    .groupby("customer_unique_id")
    .agg(
        frequency=("order_id", "count"),
        last_purchase=(
            "order_purchase_timestamp",
            "max"
        )
    )
    .reset_index()
)

rfm["recency_days"] = (
    reference_date -
    rfm["last_purchase"]
).dt.days

# =====================================================
# ORDER VALUE FEATURES
# =====================================================

order_values = (
    items.groupby("order_id")
    .agg(
        total_order_value=("price", "sum"),
        total_items=("order_item_id", "count"),
        avg_freight_cost=("freight_value", "mean")
    )
    .reset_index()
)

customer_value = (
    customer_orders[
        ["customer_unique_id", "order_id"]
    ]
    .merge(
        order_values,
        on="order_id"
    )
)

customer_value = (
    customer_value
    .groupby("customer_unique_id")
    .agg(
        monetary_value=(
            "total_order_value",
            "sum"
        ),
        avg_order_value=(
            "total_order_value",
            "mean"
        ),
        total_items_purchased=(
            "total_items",
            "sum"
        ),
        avg_freight_cost=(
            "avg_freight_cost",
            "mean"
        )
    )
    .reset_index()
)

# =====================================================
# ORDER STATUS FEATURES
# =====================================================

customer_orders["is_delivered"] = (
    customer_orders["order_status"]
    == "delivered"
).astype(int)

customer_orders["is_cancelled"] = (
    customer_orders["order_status"]
    == "canceled"
).astype(int)

status_features = (
    customer_orders
    .groupby("customer_unique_id")
    .agg(
        total_orders=("order_id", "count"),
        delivered_order_rate=(
            "is_delivered",
            "mean"
        ),
        cancelled_order_rate=(
            "is_cancelled",
            "mean"
        )
    )
    .reset_index()
)

# =====================================================
# DELIVERY FEATURES
# =====================================================

delivery = customer_orders.copy()

delivery["delivery_days"] = (
    delivery["order_delivered_customer_date"]
    -
    delivery["order_purchase_timestamp"]
).dt.days

delivery["delay_days"] = (
    delivery["order_delivered_customer_date"]
    -
    delivery["order_estimated_delivery_date"]
).dt.days

delivery["is_late"] = (
    delivery["delay_days"] > 0
).astype(int)

delivery_features = (
    delivery
    .groupby("customer_unique_id")
    .agg(
        avg_delivery_time_days=(
            "delivery_days",
            "mean"
        ),
        avg_delay_days=(
            "delay_days",
            "mean"
        ),
        late_delivery_rate=(
            "is_late",
            "mean"
        )
    )
    .reset_index()
)

# =====================================================
# PRODUCT FEATURES
# =====================================================

items_products = (
    items.merge(
        products,
        on="product_id",
        how="left"
    )
)

items_products = (
    items_products.merge(
        customer_orders[
            [
                "order_id",
                "customer_unique_id"
            ]
        ],
        on="order_id"
    )
)

product_features = (
    items_products
    .groupby("customer_unique_id")
    .agg(
        unique_products=(
            "product_id",
            "nunique"
        ),
        unique_categories=(
            "product_category_name",
            "nunique"
        ),
        unique_sellers=(
            "seller_id",
            "nunique"
        )
    )
    .reset_index()
)

# =====================================================
# REVIEW FEATURES
# =====================================================

review_data = (
    reviews.merge(
        customer_orders[
            [
                "order_id",
                "customer_unique_id"
            ]
        ],
        on="order_id"
    )
)

review_data["good_review"] = (
    review_data["review_score"] >= 4
).astype(int)

review_data["bad_review"] = (
    review_data["review_score"] <= 2
).astype(int)

review_features = (
    review_data
    .groupby("customer_unique_id")
    .agg(
        avg_review_score=(
            "review_score",
            "mean"
        ),
        good_review_rate=(
            "good_review",
            "mean"
        ),
        bad_review_rate=(
            "bad_review",
            "mean"
        )
    )
    .reset_index()
)

# =====================================================
# PAYMENT FEATURES
# =====================================================

payment_data = (
    payments.merge(
        customer_orders[
            [
                "order_id",
                "customer_unique_id"
            ]
        ],
        on="order_id"
    )
)

payment_features = (
    payment_data
    .groupby("customer_unique_id")
    .agg(
        avg_installments=(
            "payment_installments",
            "mean"
        ),
        total_payment_value=(
            "payment_value",
            "sum"
        )
    )
    .reset_index()
)

# =====================================================
# TIME FEATURES
# =====================================================

customer_orders["is_weekend"] = (
    customer_orders[
        "order_purchase_timestamp"
    ]
    .dt.dayofweek >= 5
).astype(int)

time_features = (
    customer_orders
    .groupby("customer_unique_id")
    .agg(
        weekend_purchase_ratio=(
            "is_weekend",
            "mean"
        )
    )
    .reset_index()
)

# =====================================================
# CUSTOMER STATE
# =====================================================

customer_info = (
    customers[
        [
            "customer_unique_id",
            "customer_state"
        ]
    ]
    .drop_duplicates()
)

# =====================================================
# FINAL MERGE
# =====================================================

customer_features_v3 = (
    customer_info
    .merge(rfm, on="customer_unique_id")
    .merge(customer_value, on="customer_unique_id")
    .merge(status_features, on="customer_unique_id")
    .merge(delivery_features, on="customer_unique_id")
    .merge(product_features, on="customer_unique_id")
    .merge(review_features, on="customer_unique_id")
    .merge(payment_features, on="customer_unique_id")
    .merge(time_features, on="customer_unique_id")
)

customer_features_v3.drop(
    columns=["last_purchase"],
    inplace=True
)

customer_features_v3["monthly_purchase_frequency"] = (
    customer_features_v3["frequency"] / 24
)

customer_features_v3.to_csv(
    PROCESSED_PATH /
    "customer_features_v3.csv",
    index=False
)

print("\nShape:")
print(customer_features_v3.shape)

print("\nFrequency Stats:")
print(
    customer_features_v3["frequency"]
    .describe()
)

print("\nTop Frequencies:")
print(
    customer_features_v3["frequency"]
    .value_counts()
    .head(20)
)

print("\nSaved Successfully.")