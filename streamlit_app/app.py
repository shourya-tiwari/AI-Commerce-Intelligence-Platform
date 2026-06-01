import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Commerce Intelligence Platform",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():
    customer_df = pd.read_csv(
        "data/processed/customer_segments.csv"
    )

    cluster_df = pd.read_csv(
        "data/processed/cluster_profiles.csv"
    )

    return customer_df, cluster_df


customer_df, cluster_df = load_data()

# ==========================================
# SIDEBAR
# ==========================================

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

# ==========================================
# OVERVIEW
# ==========================================

if page == "Overview":

    st.title("🛒 AI Commerce Intelligence Platform")

    st.markdown(
        """
        ### End-to-End Customer Analytics using Machine Learning

        This platform provides:
        - Customer Segmentation
        - Business Intelligence
        - Customer Personas
        - Revenue Insights
        - Explainable AI Findings
        """
    )

    total_customers = len(customer_df)

    total_revenue = customer_df[
        "monetary_value"
    ].sum()

    avg_revenue = customer_df[
        "monetary_value"
    ].mean()

    avg_review = customer_df[
        "avg_review_score"
    ].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Customers",
        f"{total_customers:,}"
    )

    col2.metric(
        "Revenue",
        f"₹{total_revenue:,.0f}"
    )

    col3.metric(
        "Avg Spend",
        f"₹{avg_revenue:.2f}"
    )

    col4.metric(
        "Avg Review",
        f"{avg_review:.2f}"
    )

    st.divider()

    st.subheader("Project Summary")

    st.write(
        """
        This project analyzes customer behavior using
        advanced machine learning techniques including:

        - PCA
        - KMeans Clustering
        - Customer Persona Discovery
        - SHAP Explainability

        Built using the Olist Brazilian E-Commerce Dataset.
        """
    )

# ==========================================
# CUSTOMER SEGMENTATION
# ==========================================

elif page == "Customer Segmentation":

    st.title("📊 Customer Segmentation")

    cluster_counts = (
        customer_df["cluster"]
        .value_counts()
        .sort_index()
    )

    st.subheader("Customer Distribution")

    st.bar_chart(cluster_counts)

    st.subheader("Cluster Profiles")

    st.dataframe(
        cluster_df,
        use_container_width=True
    )

    st.subheader("Customer Personas")

    personas = {
        0: "Loyal High-Value Customers",
        1: "Dissatisfied Customers",
        2: "Budget Buyers",
        3: "Failed Order Customers",
        4: "VIP Customers"
    }

    persona_df = pd.DataFrame({
        "Cluster": personas.keys(),
        "Persona": personas.values()
    })

    st.table(persona_df)

# ==========================================
# BUSINESS INSIGHTS
# ==========================================

elif page == "Business Insights":

    st.title("📈 Business Insights")

    st.subheader("Average Revenue by Cluster")

    revenue = (
        customer_df
        .groupby("cluster")
        ["monetary_value"]
        .mean()
    )

    st.bar_chart(revenue)

    st.subheader("Average Review Score by Cluster")

    reviews = (
        customer_df
        .groupby("cluster")
        ["avg_review_score"]
        .mean()
    )

    st.bar_chart(reviews)

    st.subheader("Average Recency by Cluster")

    recency = (
        customer_df
        .groupby("cluster")
        ["recency_days"]
        .mean()
    )

    st.bar_chart(recency)

# ==========================================
# CUSTOMER LOOKUP
# ==========================================

elif page == "Customer Lookup":

    st.title("🔍 Customer Lookup")

    customer_id = st.text_input(
        "Enter Customer Unique ID"
    )

    if customer_id:

        result = customer_df[
            customer_df[
                "customer_unique_id"
            ] == customer_id
        ]

        if not result.empty:

            st.success("Customer Found")

            customer = result.iloc[0]

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
                    f"₹{customer['monetary_value']:.2f}"
                )

                st.metric(
                    "Recency Days",
                    int(customer["recency_days"])
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
                "Customer ID not found."
            )