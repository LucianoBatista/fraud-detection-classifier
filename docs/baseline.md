---
title: Baseline
authors:
    - Luciano
---

These was the steps of my baseline using **Logistic Regression** and very simple transformations. The data was not balanced by any technique and the model was not tunned as well. 

## Pipeline

<center>
```mermaid
graph TD
  A[Raw data: fraud_detection_dataset.csv] --> B[Drop Columns];
  B[Drop Columns] --> C[Filter classes on type];
  C[Filter classes on type] --> D[Train Test Split];
  D[Train Test Split] --> E[Label Encoding on type];
  E[Label Encoding on type] --> F[Scaling];
  F[Scaling] --> G[Fit Logistic Regression];
  G[Fit Logistic Regression] --> H[Predict];
  H[Predict] --> I[Calculate Metrics];
```
</center>

