import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_customer_data

# ====================================================
# CONFIG
# ====================================================

st.set_page_config(
    page_title="AI Commerce Intelligence Platform",
    page_icon="🛒",
    layout="wide"
)

# ====================================================
# LOAD DATA
# ====================================================

customer_df, cluster_df = load_customer_data()

# ====================================================
# PERSONA MAPPING
# ====================================================

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

# ====================================================
# HEADER
# ====================================================

st.title(
    "🛒 AI Commerce Intelligence Platform"
)

st.markdown("""
### End-to-End Customer Intelligence Dashboard

Built using:

- Feature Engineering
- PCA
- KMeans Clustering
- SHAP Explainability
- Business Analytics
""")

# ====================================================
# KPIs
# ====================================================

total_customers = len(customer_df)

total_revenue = customer_df[
    "monetary_value"
].sum()

avg_spend = customer_df[
    "monetary_value"
].mean()

avg_review = customer_df[
    "avg_review_score"
].mean()

repeat_rate = (
    (customer_df["frequency"] > 1)
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
    f"{avg_spend:.2f}"
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

# ====================================================
# TOP INSIGHTS
# ====================================================

st.subheader("Key Insights")

c1, c2, c3 = st.columns(3)

with c1:
    st.success(
        "96%+ customers purchase only once"
    )

with c2:
    st.success(
        "VIP segment generates highest revenue"
    )

with c3:
    st.success(
        "Cluster is strongest predictor of customer value"
    )

st.divider()

# ====================================================
# ARCHITECTURE
# ====================================================

st.subheader(
    "Project Architecture"
)

st.code("""
Raw Olist Data
        ↓
Feature Engineering
        ↓
Customer Warehouse V3
        ↓
PCA
        ↓
KMeans Segmentation
        ↓
Customer Personas
        ↓
SHAP Explainability
        ↓
Business Dashboard
""")

st.divider()

# ====================================================
# SEGMENTATION
# ====================================================

st.subheader(
    "Customer Segmentation"
)

cluster_counts = (
    customer_df["persona"]
    .value_counts()
)

fig = px.bar(
    x=cluster_counts.index,
    y=cluster_counts.values,
    labels={
        "x":"Persona",
        "y":"Customers"
    },
    title="Customer Distribution"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# ====================================================
# PERSONAS
# ====================================================

st.subheader(
    "Customer Personas"
)

persona_df = pd.DataFrame({
    "Persona":[
        "Loyal Customers",
        "Dissatisfied Customers",
        "Budget Buyers",
        "Failed Order Customers",
        "VIP Customers"
    ],
    "Description":[
        "High value repeat customers",
        "Low satisfaction customers",
        "Low spending customers",
        "Poor delivery experience",
        "Highest spending customers"
    ]
})

st.dataframe(
    persona_df,
    width="stretch"
)

st.divider()

# ====================================================
# REVENUE ANALYSIS
# ====================================================

st.subheader(
    "Revenue by Persona"
)

revenue = (
    customer_df
    .groupby("persona")
    ["monetary_value"]
    .mean()
    .reset_index()
)

fig = px.bar(
    revenue.sort_values(
        "monetary_value",
        ascending=False
    ),
    x="persona",
    y="monetary_value",
    title="Average Revenue by Persona"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# ====================================================
# LEADERBOARD
# ====================================================

st.subheader(
    "Revenue Leaderboard"
)

leaderboard = (
    customer_df
    .groupby("persona")
    ["monetary_value"]
    .mean()
    .sort_values(
        ascending=False
    )
)

st.dataframe(
    leaderboard,
    width="stretch"
)

st.divider()

# ====================================================
# CLUSTER PROFILES
# ====================================================

st.subheader(
    "Cluster Profiles"
)

st.dataframe(
    cluster_df,
    width="stretch"
)

# ====================================================
# DOWNLOAD
# ====================================================

st.subheader(
    "Download Dataset"
)

st.download_button(
    label="Download Customer Dataset",
    data=customer_df.to_csv(
        index=False
    ),
    file_name="customer_segments.csv",
    mime="text/csv"
)

st.divider()

# ====================================================
# FOOTER
# ====================================================

st.caption(
    """
    AI Commerce Intelligence Platform

    Built with:
    Python • Streamlit • PCA • KMeans • SHAP • XGBoost
    """
)