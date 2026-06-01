import streamlit as st

st.set_page_config(
    page_title="Project Findings",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Project Findings")

st.markdown("""
Summary of discoveries made throughout the project lifecycle.
""")

# ===================================================
# PHASE 1
# ===================================================

st.header("Phase 1: Data Audit")

st.success("""
Customer ID was not the true customer identifier.

customer_unique_id was required for
accurate customer-level analysis.
""")

# ===================================================
# PHASE 2
# ===================================================

st.header("Phase 2: Feature Engineering")

st.success("""
Created a customer warehouse with
24 engineered features from:

• Orders
• Payments
• Reviews
• Products
• Sellers
• Delivery Data
""")

# ===================================================
# PHASE 3
# ===================================================

st.header("Phase 3: Exploratory Data Analysis")

st.success("""
Revenue distribution is highly skewed.

A small percentage of customers
generate a disproportionately large
amount of revenue.
""")

# ===================================================
# PHASE 4
# ===================================================

st.header("Phase 4: Preprocessing")

st.success("""
Applied:

• Median Imputation
• Log Transformation
• Standard Scaling

to prepare data for ML.
""")

# ===================================================
# PHASE 5
# ===================================================

st.header("Phase 5: PCA")

st.success("""
Reduced features from 20+ dimensions
to 11 principal components while
retaining 90% variance.
""")

# ===================================================
# PHASE 6
# ===================================================

st.header("Phase 6: Customer Segmentation")

st.success("""
Discovered 5 customer personas:

• VIP Customers
• Loyal Customers
• Budget Buyers
• Dissatisfied Customers
• Failed Order Customers
""")

# ===================================================
# PHASE 7
# ===================================================

st.header("Phase 7: Repeat Purchase Analysis")

st.warning("""
Detected Data Leakage.

High accuracy was caused by features
containing information derived from
complete customer history.
""")

# ===================================================
# PHASE 8
# ===================================================

st.header("Phase 8: High Value Customer Analysis")

st.warning("""
Further leakage investigation confirmed
that several spending features were
directly revealing customer value.
""")

# ===================================================
# PHASE 9
# ===================================================

st.header("Phase 9: SHAP Explainability")

st.success("""
Top Drivers of Customer Value:

1. Customer Segment
2. Freight Cost
3. Basket Size
4. Installments
5. Purchase Frequency
""")

# ===================================================
# FINAL CONCLUSION
# ===================================================

st.header("Final Conclusion")

st.info("""
The AI Commerce Intelligence Platform
successfully transformed raw e-commerce
data into actionable customer intelligence.

The project combines:

• Feature Engineering
• Dimensionality Reduction
• Customer Segmentation
• Explainable AI
• Business Intelligence

to provide a complete end-to-end
analytics workflow.
""")