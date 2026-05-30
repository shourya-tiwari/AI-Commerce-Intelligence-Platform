import pandas as pd
import numpy as np
from pathlib import Path

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

# -----------------------------------
# LOAD DATA
# -----------------------------------

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

translation = pd.read_csv(
    RAW_PATH / "product_category_name_translation.csv"
)

# -----------------------------------
# DATE CONVERSION
# -----------------------------------

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"]
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"]
)

# -----------------------------------
# RFM FEATURES
# -----------------------------------

reference_date = orders[
    "order_purchase_timestamp"
].max()

customer_rfm = (
    orders.groupby("customer_id")
    .agg(
        last_purchase=(
            "order_purchase_timestamp",
            "max"
        ),
        frequency=("order_id", "count")
    )
    .reset_index()
)

customer_rfm["recency_days"] = (
    reference_date -
    customer_rfm["last_purchase"]
).dt.days

# -----------------------------------
# ORDER VALUE
# -----------------------------------

order_value = (
    items.groupby("order_id")
    .agg(
        total_order_value=("price", "sum")
    )
    .reset_index()
)

order_value = (
    orders[["order_id", "customer_id"]]
    .merge(order_value, on="order_id")
)

monetary = (
    order_value.groupby("customer_id")
    .agg(
        monetary_value=(
            "total_order_value",
            "sum"
        )
    )
    .reset_index()
)

# -----------------------------------
# DELIVERY FEATURES
# -----------------------------------

delivery = orders.copy()

delivery["delivery_days"] = (
    delivery[
        "order_delivered_customer_date"
    ] -
    delivery[
        "order_purchase_timestamp"
    ]
).dt.days

delivery["delay_days"] = (
    delivery[
        "order_delivered_customer_date"
    ] -
    delivery[
        "order_estimated_delivery_date"
    ]
).dt.days

delivery["is_late"] = (
    delivery["delay_days"] > 0
).astype(int)

delivery_features = (
    delivery.groupby("customer_id")
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

# -----------------------------------
# PRODUCT FEATURES
# -----------------------------------

items_products = (
    items.merge(
        products,
        on="product_id",
        how="left"
    )
)

order_customer = orders[
    ["order_id", "customer_id"]
]

items_products = (
    items_products.merge(
        order_customer,
        on="order_id"
    )
)

product_features = (
    items_products.groupby("customer_id")
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

# -----------------------------------
# REVIEW FEATURES
# -----------------------------------

reviews = reviews.merge(
    orders[
        ["order_id", "customer_id"]
    ],
    on="order_id",
    how="left"
)

reviews["good_review"] = (
    reviews["review_score"] >= 4
).astype(int)

reviews["bad_review"] = (
    reviews["review_score"] <= 2
).astype(int)

review_features = (
    reviews.groupby("customer_id")
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

# -----------------------------------
# PAYMENT FEATURES
# -----------------------------------

payments = payments.merge(
    orders[
        ["order_id", "customer_id"]
    ],
    on="order_id"
)

payment_features = (
    payments.groupby("customer_id")
    .agg(
        avg_installments=(
            "payment_installments",
            "mean"
        )
    )
    .reset_index()
)

# -----------------------------------
# FINAL MERGE
# -----------------------------------

customer_features = (
    customers
    .merge(customer_rfm, on="customer_id")
    .merge(monetary, on="customer_id")
    .merge(delivery_features, on="customer_id")
    .merge(product_features, on="customer_id")
    .merge(review_features, on="customer_id")
    .merge(payment_features, on="customer_id")
)

customer_features.to_csv(
    PROCESSED_PATH /
    "customer_features_v2.csv",
    index=False
)

print(customer_features.shape)
print(customer_features.head())