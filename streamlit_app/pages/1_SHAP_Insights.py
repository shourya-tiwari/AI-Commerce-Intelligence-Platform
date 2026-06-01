import streamlit as st

st.set_page_config(
    page_title="SHAP Explainability",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 SHAP Explainability")

st.markdown(
    """
    Explainable AI analysis showing
    the most important factors driving
    customer value.
    """
)

st.subheader(
    "SHAP Feature Importance"
)

st.image(
    "streamlit_app/assets/shap_bar.png",
    use_container_width=True
)

st.divider()

st.subheader(
    "SHAP Summary Plot"
)

st.image(
    "streamlit_app/assets/shap_summary.png",
    use_container_width=True
)

st.divider()

st.subheader(
    "Key Insights"
)

st.success(
    """
    • Cluster membership is the strongest predictor of customer value

    • Freight cost is strongly associated with higher spending

    • Basket size contributes significantly to customer value

    • Review scores have relatively low impact on customer value
    """
)