import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_customer_data

# ====================================================
# PAGE CONFIG
# ====================================================

st.set_page_config(
    page_title="AI Commerce Intelligence Platform",
    page_icon="🛒",
    layout="wide"
)

# ====================================================
# LOAD DATA
# ====================================================

filtered_df, cluster_df = load_customer_data()

# ====================================================
# SIDEBAR
# ====================================================

st.sidebar.title("🛒 AI Commerce Intelligence")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Customer Segmentation",
        "Business Insights",
        "Customer Lookup"
    ]
)

# ====================================================
# OVERVIEW
# ====================================================

if page == "Overview":

    st.title("🛒 AI Commerce Intelligence Platform")

    st.markdown(
        """
        End-to-End Customer Intelligence System built using:

        - Feature Engineering
        - PCA
        - KMeans Clustering
        - SHAP Explainability
        - Business Analytics
        """
    )

    total_customers = len(filtered_df)

    total_revenue = filtered_df[
        "monetary_value"
    ].sum()

    avg_revenue = filtered_df[
        "monetary_value"
    ].mean()

    avg_review = filtered_df[
        "avg_review_score"
    ].mean()

    repeat_rate = (
        (filtered_df["frequency"] > 1)
        .mean()
        * 100
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Customers",
        f"{total_customers:,}"
    )

    col2.metric(
        "Revenue",
        f"{total_revenue:,.0f}"
    )

    col3.metric(
        "Avg Spend",
        f"{avg_revenue:.2f}"
    )

    col4.metric(
        "Avg Review",
        f"{avg_review:.2f}"
    )

    col5.metric(
        "Repeat Rate",
        f"{repeat_rate:.2f}%"
    )

    st.divider()

    st.subheader("Key Findings")

    st.info(
        """
        • More than 96% of customers purchased only once

        • Customer segmentation identified 5 distinct personas

        • Cluster membership is the strongest predictor of customer value

        • Revenue is concentrated among a small VIP segment

        • Delivery performance strongly affects customer satisfaction
        """
    )

    st.download_button(
        label="Download Customer Dataset",
        data=filtered_df.to_csv(
            index=False
        ),
        file_name="customer_segments.csv",
        mime="text/csv"
    )

# ====================================================
# CUSTOMER SEGMENTATION
# ====================================================

elif page == "Customer Segmentation":

    st.title("📊 Customer Segmentation")

    cluster_counts = (
        filtered_df["cluster"]
        .value_counts()
        .sort_index()
    )

    fig = px.bar(
        x=cluster_counts.index,
        y=cluster_counts.values,
        labels={
            "x": "Cluster",
            "y": "Customers"
        },
        title="Customer Distribution by Cluster"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Customer Personas")

    personas = {
        0: "Loyal High Value Customers",
        1: "Dissatisfied Customers",
        2: "Budget Buyers",
        3: "Failed Order Customers",
        4: "VIP Customers"
    }

    for cluster, persona in personas.items():

        st.markdown(
            f"### Cluster {cluster}: {persona}"
        )

    st.divider()

    st.subheader("Cluster Profiles")

    st.dataframe(
        cluster_df,
        use_container_width=True
    )

# ====================================================
# BUSINESS INSIGHTS
# ====================================================

elif page == "Business Insights":

    selected_clusters = st.multiselect(
        "Select Clusters",
        sorted(
            filtered_df["cluster"]
            .unique()
        ),
        default=sorted(
            filtered_df["cluster"]
            .unique()
        )
    )

    filtered_df = filtered_df[
        filtered_df["cluster"]
        .isin(selected_clusters)
    ]

    st.title("📈 Business Insights")

    revenue = (
        filtered_df
        .groupby("cluster")
        ["monetary_value"]
        .mean()
        .reset_index()
    )

    fig1 = px.bar(
        revenue,
        x="cluster",
        y="monetary_value",
        title="Average Revenue by Cluster"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    reviews = (
        filtered_df
        .groupby("cluster")
        ["avg_review_score"]
        .mean()
        .reset_index()
    )

    fig2 = px.bar(
        reviews,
        x="cluster",
        y="avg_review_score",
        title="Average Review Score by Cluster"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    recency = (
        filtered_df
        .groupby("cluster")
        ["recency_days"]
        .mean()
        .reset_index()
    )

    fig3 = px.bar(
        recency,
        x="cluster",
        y="recency_days",
        title="Average Recency by Cluster"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# ====================================================
# CUSTOMER LOOKUP
# ====================================================

elif page == "Customer Lookup":

    st.title("🔍 Customer Lookup")

    customer_id = st.text_input(
        "Enter Customer Unique ID"
    )

    if customer_id:

        result = filtered_df[
            filtered_df[
                "customer_unique_id"
            ] == customer_id
        ]

        if not result.empty:

            customer = result.iloc[0]

            st.success(
                "Customer Found"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Cluster",
                    int(customer["cluster"])
                )

                st.metric(
                    "Frequency",
                    int(customer["frequency"])
                )

                st.metric(
                    "Review Score",
                    round(
                        customer["avg_review_score"],
                        2
                    )
                )

            with col2:

                st.metric(
                    "Monetary Value",
                    round(
                        customer["monetary_value"],
                        2
                    )
                )

                st.metric(
                    "Recency",
                    int(
                        customer["recency_days"]
                    )
                )

                st.metric(
                    "Installments",
                    round(
                        customer["avg_installments"],
                        2
                    )
                )

            st.divider()

            st.dataframe(
                result,
                use_container_width=True
            )

        else:

            st.error(
                "Customer not found"
            )