# AI Commerce Intelligence Platform
# Key Findings & Business Insights Report

---

# Executive Summary

This report documents the key findings, discoveries, and business insights generated throughout the development of the AI Commerce Intelligence Platform using the Olist Brazilian E-Commerce Dataset.

The project progressed through multiple stages including:

- Data Auditing
- Feature Engineering
- Exploratory Data Analysis
- Data Preprocessing
- PCA Dimensionality Reduction
- Customer Segmentation
- Customer Behavior Analysis
- High Value Customer Identification
- SHAP Explainability

The goal was not only to build machine learning models but also to derive meaningful business insights that can support customer retention, marketing, and operational decision-making.

---

# Phase 1: Data Audit & Understanding

## Objective

Understand the structure and relationships between the Olist datasets.

## Key Findings

- Olist data is distributed across multiple relational tables.
- Customer, orders, products, reviews, payments, and seller information are stored separately.
- Significant preprocessing and feature engineering were required before machine learning could be applied.

## Major Discovery

### Customer Identification Issue

Initially, customer-level analysis was performed using:

```text
customer_id
```

However, investigation revealed that:

```text
customer_id
```

does not uniquely represent a customer.

The correct identifier is:

```text
customer_unique_id
```

This discovery prevented incorrect customer analysis and significantly improved feature engineering quality.

---

# Phase 2: Customer Feature Engineering

## Objective

Build a customer-centric analytical warehouse.

## Customer Warehouse V3

Created a feature warehouse containing:

- RFM Features
- Review Features
- Payment Features
- Delivery Features
- Product Features
- Seller Features
- Behavioral Features

Final Dataset:

- Customer Level Granularity
- 24 Engineered Features

## Major Discovery

### Extremely Low Customer Retention

Frequency analysis revealed:

- More than 96% of customers purchased only once.
- Very few customers placed multiple orders.

Business Interpretation:

The Olist marketplace experiences low customer retention and limited repeat purchasing behavior.

---

# Phase 3: Exploratory Data Analysis

## Objective

Understand customer behavior and feature distributions.

---

## Monetary Value Analysis

Key Findings:

- Highly right-skewed distribution.
- Small number of customers contribute significantly higher revenue.

Statistics:

- Median Spending ≈ 89
- Maximum Spending ≈ 13,440

Business Insight:

A relatively small group of customers contributes a disproportionately large share of revenue.

---

## Delivery Analysis

Key Findings:

- Delivery times vary considerably.
- Late deliveries occur across the platform.

Business Insight:

Delivery performance may influence customer experience and retention.

---

## Review Analysis

Key Findings:

Average Review Score:

```text
≈ 4.1 / 5
```

Business Insight:

Overall customer satisfaction is generally positive.

---

# Phase 4: Data Preprocessing

## Objective

Prepare data for machine learning.

## Transformations Applied

### Missing Value Handling

Applied:

- Median Imputation

Missing Features:

- Average Delivery Time
- Average Delay Days

---

### Feature Transformation

Applied:

- Log Transformation

Features:

- Monetary Value
- Average Order Value
- Total Payment Value
- Freight Cost

---

### Feature Scaling

Applied:

- StandardScaler

Business Impact:

Improved machine learning performance and reduced skewness effects.

---

# Phase 5: PCA Dimensionality Reduction

## Objective

Reduce dimensionality while preserving information.

## Results

Original Features:

```text
20
```

Reduced Features:

```text
11
```

Variance Retained:

```text
90%
```

## Key Finding

Customer behavior can be represented effectively using a smaller set of dimensions.

Business Impact:

Reduced model complexity while retaining most behavioral information.

---

# Phase 6: Customer Segmentation

## Objective

Identify customer groups with similar behavior.

## Methodology

Algorithm:

```text
KMeans Clustering
```

Selected:

```text
K = 5
```

Using:

- Elbow Method
- Silhouette Analysis
- Business Interpretability

---

## Customer Personas

### Cluster 0

Loyal High-Value Customers

Characteristics:

- High spending
- Excellent reviews
- Consistent purchasing behavior

---

### Cluster 1

Dissatisfied Customers

Characteristics:

- Poor review scores
- Higher dissatisfaction indicators

---

### Cluster 2

Budget Buyers

Characteristics:

- Lowest spending
- Limited engagement
- Mostly one-time purchases

---

### Cluster 3

Failed Order Customers

Characteristics:

- Extremely poor delivery success
- Low customer satisfaction

---

### Cluster 4

VIP Customers

Characteristics:

- Highest spending
- Highest purchase frequency
- Largest basket size

---

## Major Discovery

Customer base is highly heterogeneous.

Different customer groups require different retention and marketing strategies.

---

# Phase 7: Repeat Purchase Behavior Analysis

## Objective

Analyze behavioral characteristics of repeat buyers.

## Key Finding

The model achieved extremely high performance.

Further investigation revealed:

```text
Data Leakage
```

because features were generated using complete customer histories.

## Important Lesson

High model accuracy does not necessarily imply predictive value.

Understanding how features are generated is critical in machine learning projects.

---

# Phase 8: High Value Customer Identification

## Objective

Identify customers belonging to the highest spending segment.

## Key Finding

Near-perfect model performance was achieved.

Further analysis revealed that customer value was already embedded in several engineered features.

## Important Lesson

Feature leakage can significantly inflate model performance.

Careful feature design is essential for reliable predictive modeling.

---

# Phase 9: SHAP Explainability

## Objective

Understand the factors driving customer value.

## Most Important Discovery

The strongest predictor of customer value was:

```text
Customer Segment (Cluster)
```

This validates the effectiveness of the customer segmentation pipeline.

---

## Top Drivers of Customer Value

1. Customer Segment
2. Average Freight Cost
3. Total Items Purchased
4. Average Installments
5. Purchase Frequency

---

## Surprising Discovery

Review-related features had relatively low impact on customer value.

Examples:

- Average Review Score
- Good Review Rate
- Bad Review Rate

Business Insight:

Customer satisfaction and customer value are not necessarily the same thing.

---

## Business Interpretation

Customer value is driven primarily by:

- Spending behavior
- Basket size
- Product purchasing patterns
- Segment membership

rather than customer sentiment.

---

# Overall Project Learnings

## Technical Learnings

- Feature engineering often matters more than model selection.
- Data leakage can create misleading model performance.
- PCA effectively reduces dimensionality without significant information loss.
- Customer segmentation provides valuable business context for downstream analysis.
- SHAP explainability helps translate machine learning outputs into actionable insights.

---

## Business Learnings

- Customer retention is extremely low.
- Revenue is concentrated among a small group of customers.
- Delivery performance significantly impacts customer experience.
- Customer segments exhibit substantially different behaviors.
- High-value customers can be characterized using behavioral patterns rather than review sentiment alone.

---

# Final Conclusion

The AI Commerce Intelligence Platform successfully transformed raw e-commerce data into actionable customer intelligence.

Through advanced feature engineering, segmentation, explainability, and behavioral analysis, the project identified meaningful customer personas and business insights that can support:

- Customer Retention
- Marketing Optimization
- Revenue Growth
- Customer Experience Improvement
- Strategic Decision Making

The resulting platform demonstrates an end-to-end machine learning and analytics workflow suitable for real-world business applications.