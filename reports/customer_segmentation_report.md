# Customer Segmentation Report

## Project Overview

This report presents the customer segmentation analysis performed on the Olist Brazilian E-Commerce dataset. The objective was to identify distinct customer groups based on purchasing behavior, delivery experience, product interactions, payment behavior, and customer satisfaction metrics.

The segmentation pipeline involved advanced feature engineering, preprocessing, dimensionality reduction, and unsupervised machine learning techniques.

---

# Dataset Overview

### Original Dataset

The Olist dataset consists of multiple interconnected e-commerce tables containing:

* Customer information
* Orders
* Products
* Sellers
* Payments
* Reviews

### Customer Warehouse

A customer-centric feature warehouse was created using `customer_unique_id` as the primary identifier.

### Final Dataset

* Total Customers: 44,787
* Features Engineered: 24
* Granularity: 1 row = 1 customer

---

# Feature Engineering

The following categories of features were engineered:

## RFM Features

* Frequency
* Recency Days
* Monetary Value
* Average Order Value

## Order Features

* Total Orders
* Delivered Order Rate
* Cancelled Order Rate

## Product Features

* Unique Products Purchased
* Unique Categories Purchased
* Total Items Purchased

## Seller Features

* Unique Sellers

## Delivery Features

* Average Delivery Time
* Average Delay Days
* Late Delivery Rate
* Average Freight Cost

## Review Features

* Average Review Score
* Good Review Rate
* Bad Review Rate

## Payment Features

* Average Installments
* Total Payment Value

## Time Features

* Weekend Purchase Ratio
* Monthly Purchase Frequency

---

# Data Preprocessing

The following preprocessing steps were applied:

## Missing Value Handling

Median imputation was applied to:

* Average Delivery Time
* Average Delay Days

## Feature Transformation

Log transformation was applied to:

* Monetary Value
* Average Order Value
* Total Payment Value
* Average Freight Cost

## Feature Scaling

StandardScaler was used to normalize all numerical features before clustering.

---

# Dimensionality Reduction

Principal Component Analysis (PCA) was applied to reduce dimensionality while preserving information.

### Results

* Original Features: 20
* PCA Components Retained: 11
* Variance Explained: 90%

This reduced computational complexity while preserving most customer behavior information.

---

# Clustering Methodology

## Algorithm

K-Means Clustering

### Hyperparameters

* Number of Clusters (K): 5
* Random State: 42
* n_init: 20

The value of K was selected using:

* Elbow Method
* Silhouette Analysis
* Business Interpretability

---

# Cluster Distribution

| Cluster | Customers |
| ------- | --------: |
| 0       |    15,575 |
| 1       |     5,775 |
| 2       |    20,523 |
| 3       |       973 |
| 4       |     1,941 |

---

# Cluster Analysis

## Cluster 0 – Loyal High-Value Customers

Characteristics:

* High spending behavior
* Excellent review scores
* High delivery success rate
* Consistent purchasing behavior

Average Metrics:

* Monetary Value: 244.58
* Review Score: 4.61

Business Value:

This group represents highly satisfied and valuable customers.

Recommendations:

* Loyalty programs
* Personalized recommendations
* Early access offers

---

## Cluster 1 – Dissatisfied Customers

Characteristics:

* Moderate spending
* Extremely poor review scores
* High dissatisfaction indicators

Average Metrics:

* Monetary Value: 145.47
* Review Score: 1.45

Business Value:

This group is at high risk of permanent churn.

Recommendations:

* Customer support intervention
* Complaint resolution campaigns
* Service quality improvements

---

## Cluster 2 – Budget Buyers

Characteristics:

* Lowest spending behavior
* Minimal engagement
* Mostly one-time purchases

Average Metrics:

* Monetary Value: 52.72
* Review Score: 4.59

Business Value:

Large customer population with low revenue contribution.

Recommendations:

* Upselling campaigns
* Cross-selling opportunities
* Discount-based engagement

---

## Cluster 3 – Failed Order Customers

Characteristics:

* Very low delivery success rate
* Poor review scores
* Highest recency value

Average Metrics:

* Monetary Value: 190.06
* Review Score: 1.72
* Delivered Order Rate: 0.02

Business Value:

Represents customers negatively impacted by operational issues.

Recommendations:

* Logistics improvements
* Delivery recovery campaigns
* Refund and retention strategies

---

## Cluster 4 – VIP Customers

Characteristics:

* Highest spending behavior
* Highest purchase frequency
* Largest basket sizes

Average Metrics:

* Monetary Value: 272.51
* Frequency: 1.99

Business Value:

Most profitable customer segment.

Recommendations:

* Premium membership programs
* Exclusive offers
* Priority customer support

---

# Key Business Insights

### Insight 1

Customer spending varies significantly across segments, indicating the presence of high-value and low-value customer groups.

### Insight 2

Customer satisfaction is strongly associated with delivery success.

### Insight 3

A small group of VIP customers contributes disproportionately high revenue.

### Insight 4

Operational failures create a distinct customer segment with poor satisfaction scores.

### Insight 5

Most customers make only a single purchase, indicating retention opportunities.

---

# Artifacts Generated

## Datasets

* customer_features_v3.csv
* customer_segments.csv
* cluster_profiles.csv

## Models

* kmeans_customer_segmentation.pkl
* customer_pca.pkl
* customer_imputer.pkl
* customer_scaler.pkl

---

# Conclusion

The customer segmentation pipeline successfully identified five distinct customer personas within the Olist marketplace.

These segments provide actionable business insights for marketing, customer retention, logistics optimization, and revenue growth initiatives.

The resulting customer personas can be leveraged in future machine learning applications including repeat purchase prediction, customer lifetime value estimation, anomaly detection, and recommendation systems.
