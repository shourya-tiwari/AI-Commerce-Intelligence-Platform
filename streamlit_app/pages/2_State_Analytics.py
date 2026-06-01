import streamlit as st
import plotly.express as px

from utils.data_loader import load_customer_data

customer_df, _ = load_customer_data()

st.set_page_config(
    page_title="State Analytics",
    page_icon="🌎",
    layout="wide"
)

st.title("🌎 State-wise Analytics")

metric = st.selectbox(
    "Select Metric",
    [
        "monetary_value",
        "avg_review_score",
        "frequency"
    ]
)

state_summary = (
    customer_df
    .groupby("customer_state")
    .agg({
        "monetary_value":"mean",
        "avg_review_score":"mean",
        "frequency":"mean"
    })
    .reset_index()
)

fig = px.bar(
    state_summary.sort_values(
        metric,
        ascending=False
    ),
    x="customer_state",
    y=metric,
    title=f"{metric} by State"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader(
    "State Statistics"
)

st.dataframe(
    state_summary,
    use_container_width=True
)