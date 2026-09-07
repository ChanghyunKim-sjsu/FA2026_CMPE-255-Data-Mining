# CMPE 255 — Assignment 1

## AI-Assisted Data Science

This repository contains my work for CMPE 255 Assignment 1.

The assignment explores how an agentic AI coding assistant can support an
end-to-end data science workflow while the student remains responsible for
executing, validating, understanding, and explaining the results.

The project is organized into two parts:

- **Part 1:** AI-assisted end-to-end data science using a Kaggle dataset
- **Part 2:** Replication of selected data science experiments from the
  professor's `data_science_examples` repository

---

# Part 1 — House Price Prediction

## Project Overview

For Part 1, I used the Kaggle **House Prices: Advanced Regression Techniques**
dataset to build a supervised machine learning workflow for predicting
residential sale prices.

The target variable is:

`SalePrice`

The analysis follows a workflow inspired by CRISP-DM:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Interpretation and Communication

AI tools were used to assist with planning, code generation, debugging,
analysis, and documentation. However, generated code and results were executed,
checked, and interpreted before being included in the final project.

---

## Dataset

The training dataset contains:

- **1,460 observations**
- **81 columns**
- Numerical and categorical features
- **0 duplicate rows**

The target variable `SalePrice` is strongly right-skewed, with a skewness of
approximately **1.88**.

An important part of the data-cleaning process was investigating missing
values. Several values that initially appeared to be missing actually represented
the absence of property features.

Examples include:

- `PoolQC = NA` → no pool
- `GarageType = NA` → no garage
- `BsmtQual = NA` → no basement
- `MasVnrType = None` → no masonry veneer

This investigation helped avoid incorrectly treating meaningful property
information as generic missing data.

---

## Exploratory Data Analysis

The numerical features most strongly correlated with `SalePrice` included:

- `OverallQual` — approximately **0.79**
- `GrLivArea` — approximately **0.71**
- `GarageCars` — approximately **0.64**
- `GarageArea` — approximately **0.62**
- `TotalBsmtSF` — approximately **0.61**

The analysis suggests that overall property quality and usable living space
are strongly associated with house sale prices.

---

## Data Preparation

The preprocessing workflow handled numerical and categorical variables
separately.

Numerical features were processed using:

- Missing-value imputation
- Feature scaling where appropriate

Categorical features were processed using:

- Domain-aware missing-value handling
- Missing-value imputation where necessary
- One-hot encoding

Scikit-learn `Pipeline` and `ColumnTransformer` were used to make the
preprocessing and modeling workflow reproducible.

---

## Models Evaluated

Four regression approaches were evaluated:

1. Dummy Regressor
2. Ridge Regression
3. Random Forest Regressor
4. Gradient Boosting Regressor

The Dummy Regressor was used as a baseline so that the machine learning
models could be compared against a simple average-price prediction strategy.

The complete model comparison is available here:

[`results/model_comparison.csv`](Part-1/house-prices/results/model_comparison.csv)

---

## Best Model — Gradient Boosting

Gradient Boosting achieved the strongest validation performance.

Approximate validation results:

- **RMSE:** $27,790
- **MAE:** $17,165
- **R²:** 0.899

The model substantially outperformed the Dummy baseline, which produced an
RMSE of approximately $87,619.

---

## Cross-Validation

To determine whether the Gradient Boosting performance depended heavily on
one train-validation split, I also performed 5-fold cross-validation.

Results:

- **Mean CV RMSE:** approximately $26,871
- **Standard deviation:** approximately $3,651

The cross-validation result was similar to the original validation result,
providing additional evidence that the model generalizes reasonably well
across different subsets of the dataset.

Detailed results:

[`results/cross_validation_rmse.csv`](Part-1/house-prices/results/cross_validation_rmse.csv)

---

## Model Interpretation

The Gradient Boosting feature-importance analysis identified the following as
some of the strongest predictive features:

- `OverallQual` — approximately 50% of total feature importance
- `GrLivArea` — approximately 15%
- `GarageCars`
- `TotalBsmtSF`
- `BsmtFinSF1`
- `1stFlrSF`

These findings are consistent with the earlier correlation analysis.

Feature importance describes how the model uses variables for prediction and
should not be interpreted as evidence of causation.

---

## Prediction Error Analysis

Although the final model performed well overall, some individual predictions
contained large errors.

Several of the largest underpredictions occurred for expensive homes. For
example, one property sold for approximately $611,657 but was predicted at
approximately $403,266.

This suggests that unusual or high-priced properties may contain
characteristics that are more difficult for the model to capture.

The complete prediction-error results are available here:

[`results/prediction_errors.csv`](Part-1/house-prices/results/prediction_errors.csv)

---

## Visualizations

### SalePrice Distribution

![SalePrice Distribution](Part-1/house-prices/figures/saleprice_distribution.png)

### Missing Values

![Missing Values](Part-1/house-prices/figures/missing_values.png)

### Numerical Correlations

![Top Correlations](Part-1/house-prices/figures/top_correlations.png)

### Actual vs Predicted Prices

![Actual vs Predicted](Part-1/house-prices/figures/actual_vs_predicted.png)

### Gradient Boosting Feature Importance

![Feature Importance](Part-1/house-prices/figures/feature_importance.png)

---

## Part 1 Project Artifacts

### Notebook

[`house_prices_analysis.ipynb`](Part-1/house-prices/notebooks/house_prices_analysis.ipynb)

The final notebook was restarted and executed from beginning to end to verify
that the analysis is reproducible.

### Dataset

[`train.csv`](Part-1/house-prices/data/train.csv)

### Results

- [`model_comparison.csv`](Part-1/house-prices/results/model_comparison.csv)
- [`cross_validation_rmse.csv`](Part-1/house-prices/results/cross_validation_rmse.csv)
- [`prediction_errors.csv`](Part-1/house-prices/results/prediction_errors.csv)
- [`feature_importance.csv`](Part-1/house-prices/results/feature_importance.csv)

### Project Planning

- [`intent.md`](Part-1/house-prices/intent.md)
- [`spec.md`](Part-1/house-prices/spec.md)
- [`plan.md`](Part-1/house-prices/plan.md)

These planning documents are supplemental artifacts used to organize the
AI-assisted workflow.

---

## AI-Assisted Workflow

The AI assistant was used for tasks such as:

- Planning the data science workflow
- Suggesting exploratory analysis
- Generating Python code
- Debugging notebook issues
- Designing preprocessing pipelines
- Comparing regression models
- Interpreting model results
- Organizing documentation

AI output was not accepted blindly.

For example, during missing-value analysis, additional inspection revealed
that Pandas' default parsing behavior could interpret meaningful values such
as `NA` and `None` as missing data. The preprocessing approach was adjusted
after examining the actual domain meaning of those values.

The final explanations in this project are based on my interpretation of the
executed results.

---

# Part 2 — Data Science Experiment Replication

Part 2 will replicate selected experiments from the professor's
`data_science_examples` repository using an AI coding assistant.

The planned experiments are:

### Customer Segmentation

Location:

`Part-2/customer-segmentation/`

### Market Basket Analysis

Location:

`Part-2/market-basket-analysis/`

### Anomaly Detection

Location:

`Part-2/anomaly-detection/`

Part 2 results and artifacts will be added after each experiment is executed
and validated.

---

# YouTube Walkthrough

The final Assignment 1 walkthrough will explain the end-to-end AI-assisted
data science process and the results in my own words.

**YouTube Link:** To be added after recording.

---

# Assignment Status

## Part 1

**Analysis complete**

The House Prices notebook, figures, results, and supporting project artifacts
are included in this repository.

## Part 2

**In progress**

The experiment replication artifacts will be added before final submission.

---

## Author

Changhyun Kim  
San José State University  
CMPE 255 — Data Mining  
Fall 2026
