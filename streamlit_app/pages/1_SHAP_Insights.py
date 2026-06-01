import streamlit as st

st.set_page_config(
    page_title="Explainable AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Explainable AI")

st.markdown("""
Understanding the factors that drive customer value using SHAP Explainability.
""")

st.subheader(
    "Feature Importance"
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
    "Business Interpretation"
)

col1, col2 = st.columns(2)

with col1:

    st.success("""
    Cluster membership is the strongest predictor
    of customer value.
    """)

    st.success("""
    VIP customers contribute the most revenue.
    """)

with col2:

    st.success("""
    Freight cost is strongly associated with
    customer spending.
    """)

    st.success("""
    Review scores have relatively low impact
    on customer value.
    """)