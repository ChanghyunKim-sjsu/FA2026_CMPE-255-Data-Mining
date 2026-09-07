# AI-Assisted Workflow Summary

## CMPE 255 Assignment 1 - Part 1: House Prices

This document provides an English summary of the AI-assisted workflow used for
Part 1 of CMPE 255 Assignment 1. It is a guide to the project process and final
artifacts; it does not replace, translate, or reconstruct the original ChatGPT
conversation. The original export is preserved separately as
`original_chat_transcript.pdf`.

## Project Objective

The project used the Kaggle **House Prices: Advanced Regression Techniques**
dataset to build a supervised regression workflow for predicting residential
`SalePrice`. The analysis followed the CRISP-DM framework and emphasized both
predictive performance and an understandable account of how the result was
produced.

## How AI Assisted the Work

ChatGPT supported the project by:

- helping define the prediction problem and CRISP-DM analysis plan;
- suggesting exploratory analyses and visualizations;
- generating and explaining Python code;
- helping diagnose notebook and data-loading issues;
- designing preprocessing pipelines for mixed data types;
- comparing regression models and evaluation metrics;
- interpreting prediction errors and feature importance;
- helping organize the notebook, results, and repository documentation.

AI suggestions were reviewed against the dataset and executed notebook outputs
before being included in the final project.

## CRISP-DM Workflow

### 1. Business Understanding

The project defined the task as predicting the sale price of a house from its
physical characteristics, quality, location, and related attributes. The target
was `SalePrice`, making this a supervised regression problem. Model performance
was evaluated with RMSE, MAE, and R-squared, with RMSE used for the final model
comparison and cross-validation.

### 2. Data Understanding

The training data contained:

- 1,460 observations;
- 81 columns;
- numerical and categorical variables;
- 0 duplicate rows;
- no missing target values.

The target distribution was strongly right-skewed, with skewness of
approximately 1.88. Exploratory analysis examined its distribution, missing
values, numerical correlations, categorical relationships, and unusual houses.
The strongest numerical relationships with sale price included `OverallQual`,
`GrLivArea`, `GarageCars`, `GarageArea`, and `TotalBsmtSF`.

### 3. Domain-Aware Data Preparation

A key finding was that Pandas' default CSV parsing can interpret literal values
such as `NA` and `None` as generic missing values. In the Kaggle data dictionary,
many of these values describe the absence of a property feature rather than an
unknown observation. The data was therefore reloaded with
`keep_default_na=False` and cleaned using domain-specific labels such as:

- `NoPool`;
- `NoGarage`;
- `NoBasement`;
- `NoMasonryVeneer`;
- `NoFireplace`.

Remaining true missing values were retained for pipeline-based imputation. The
final modeling workflow used an 80/20 training-validation split with
`random_state=42`. Numerical variables were median-imputed and standardized.
Categorical variables were imputed with the most frequent value and one-hot
encoded, with previously unseen categories ignored.

### 4. Modeling

Four regression approaches were evaluated with consistent preprocessing:

1. Dummy Regressor as a simple mean-price baseline
2. Ridge Regression
3. Random Forest Regressor
4. Gradient Boosting Regressor

The baseline established whether the machine-learning models added meaningful
predictive value. Ridge tested a regularized linear relationship, while Random
Forest and Gradient Boosting represented nonlinear tree-based approaches.

### 5. Evaluation

The final validation results recorded in `results/model_comparison.csv` were:

| Model | RMSE | MAE | R-squared |
|---|---:|---:|---:|
| Gradient Boosting | $27,790 | $17,165 | 0.899 |
| Random Forest | $29,024 | $17,495 | 0.890 |
| Ridge Regression | $29,721 | $19,101 | 0.885 |
| Dummy Baseline | $87,619 | $62,576 | -0.001 |

Gradient Boosting achieved the best validation performance. Five-fold
cross-validation produced a mean RMSE of approximately $26,871 with a standard
deviation of approximately $3,651, supporting the conclusion that its result
was not dependent on only one train-validation split.

### 6. Interpretation and Communication

Feature-importance analysis identified the most influential predictors used by
the Gradient Boosting model:

- `OverallQual`, approximately 50.2% of total importance;
- `GrLivArea`, approximately 15.4%;
- `GarageCars`;
- `TotalBsmtSF`;
- `BsmtFinSF1`;
- `1stFlrSF`.

These findings were consistent with the earlier correlation analysis. Feature
importance was interpreted as predictive usefulness, not evidence of causation.

Prediction-error analysis showed that some expensive or unusual homes were
substantially underpredicted. The largest recorded absolute error involved a
home that sold for $611,657 but was predicted at approximately $403,266. This
suggests that rare high-value properties are more difficult for the model to
represent accurately.

For this academic project, the CRISP-DM deployment phase was treated as clear
communication through the executed notebook, saved figures, CSV result tables,
repository documentation, and planned video walkthrough rather than deployment
of a production service.

## Human Validation

The final notebook was restarted, run from beginning to end, and saved. Its 51
code cells all contain execution counts. The generated results were reviewed
against the CSV files and README, and the final interpretation was written from
the observed outputs rather than accepted from AI suggestions without checking.

The project also records an important human correction: investigation of the
data dictionary and raw CSV values changed how `NA` and `None` were interpreted.
This prevented meaningful absence categories from being treated automatically
as ordinary missing data.

## Transcript Provenance

`original_chat_transcript.pdf` is a byte-for-byte copy of the original
61-page ChatGPT Exporter PDF that was already present in this repository as
`Assignment1/Chat_transcript.pdf`. The export includes the original conversation
URL and spans the initial House Prices discussion through its CRISP-DM
conclusions. No messages were translated, rewritten, or synthesized for that
PDF.

The preserved transcript documents an earlier iteration of the analysis, so
some model choices and recorded metrics differ from the final executed notebook.
The notebook and CSV files under this `Assignment 1/Part-1/house-prices/`
directory are the authoritative sources for the final submitted results.
