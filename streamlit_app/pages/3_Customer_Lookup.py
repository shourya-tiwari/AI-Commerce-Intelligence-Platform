import streamlit as st
import pandas as pd

from utils.data_loader import load_customer_data

st.set_page_config(
    page_title="Customer Lookup",
    page_icon="🔍",
    layout="wide"
)

customer_df, _ = load_customer_data()

persona_map = {
    0: "Loyal Customers",
    1: "Dissatisfied Customers",
    2: "Budget Buyers",
    3: "Failed Order Customers",
    4: "VIP Customers"
}

customer_df["persona"] = (
    customer_df["cluster"]
    .map(persona_map)
)

st.title("🔍 Customer Lookup")

st.markdown("""
Search for an individual customer and view their profile.
""")

customer_id = st.text_input(
    "Enter Customer Unique ID"
)

if customer_id:

    result = customer_df[
        customer_df["customer_unique_id"]
        == customer_id
    ]

    if not result.empty:

        customer = result.iloc[0]

        st.success(
            "Customer Found"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Persona",
                customer["persona"]
            )

            st.metric(
                "Frequency",
                int(customer["frequency"])
            )

            st.metric(
                "Recency",
                int(customer["recency_days"])
            )

        with col2:

            st.metric(
                "Monetary Value",
                f"{customer['monetary_value']:.2f}"
            )

            st.metric(
                "Review Score",
                f"{customer['avg_review_score']:.2f}"
            )

            st.metric(
                "Installments",
                f"{customer['avg_installments']:.2f}"
            )

        with col3:

            st.metric(
                "Products",
                int(customer["unique_products"])
            )

            st.metric(
                "Categories",
                int(customer["unique_categories"])
            )

            st.metric(
                "Sellers",
                int(customer["unique_sellers"])
            )

        st.divider()

        st.subheader(
            "Complete Customer Record"
        )

        st.dataframe(
            result,
            width="stretch"
        )

    else:

        st.error(
            "Customer ID not found."
        )