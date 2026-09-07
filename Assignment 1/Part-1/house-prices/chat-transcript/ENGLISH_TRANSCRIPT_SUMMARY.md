# English Summary of the AI-Assisted Session

## CMPE 255 — Assignment 1, Part 1
### AI-Assisted House Price Prediction

**Original Session Date:** September 6, 2026

The original AI-assisted session was conducted primarily in Korean.
This document provides an English summary of the actual September 6 session.

This is not a word-for-word translation.
The original Korean transcript is preserved separately as the source record.

---

## 1. Restarting the Assignment

The session began by deciding to rebuild Assignment 1 from the beginning.

Earlier work was kept only as backup material. The new project would use only
results produced by the new final notebook run.

The working principle was:

Professor Requirements
→ intent.md
→ spec.md
→ plan.md
→ Notebook / Code
→ Validation
→ Results
→ README
→ YouTube

The goal was not only to generate a machine-learning result, but also to create
a reproducible AI-assisted data science workflow that I could explain in my own
words.

---

## 2. Project Organization

The final working directory was organized under:

`Assignment 1/`

Part 1 used:

`Part-1/house-prices/`

with the following structure:

- `intent.md`
- `spec.md`
- `plan.md`
- `data/`
- `notebooks/`
- `figures/`
- `results/`
- `chat-transcript/`
- `report/`

Older folders were preserved as backups while `Assignment 1` became the final
working directory.

---

## 3. Intent, Specification, and Plan

Three planning documents were created before modeling.

### intent.md

Defined why the project was being performed:

- predict residential house prices
- use the Kaggle House Prices dataset
- use AI throughout the workflow
- validate AI-generated output rather than accepting it blindly
- explain final results in my own words

### spec.md

Defined what the analysis should contain:

- supervised regression
- target variable: `SalePrice`
- dataset validation
- exploratory data analysis
- numerical and categorical preprocessing
- baseline model
- multiple regression models
- RMSE, MAE, and R²
- cross-validation
- prediction-error analysis
- feature interpretation
- reproducibility checks

### plan.md

Converted the specification into an implementation checklist covering:

- project setup
- data understanding
- EDA
- data preparation
- baseline modeling
- model comparison
- interpretation
- final validation
- documentation
- assignment deliverables

---

## 4. Python and Jupyter Environment

The analysis was performed locally using:

- VS Code
- Jupyter Notebook
- Python virtual environment
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

During setup, the notebook initially used the wrong Python environment.

The selected interpreter pointed to a previous CMPE 272 project:

`CMPE-272-Enterprise-Software-Platforms/Assignment 2/.venv/bin/python`

A dedicated CMPE 255 kernel was then installed and registered as:

`CMPE 255 House Prices`

The final notebook interpreter was verified as:

`.../CMPE-255/FA2026_CMPE-255-Data-Mining/Assignment 1/Part-1/house-prices/.venv/bin/python`

This ensured that the CMPE 255 notebook used its own isolated Python environment.

---

## 5. Dataset Understanding

The project used the Kaggle:

**House Prices: Advanced Regression Techniques**

training dataset.

Initial inspection produced:

- Rows: 1,460
- Columns: 81
- String columns: 43
- Integer columns: 35
- Float columns: 3
- Duplicate rows: 0

The prediction target was:

`SalePrice`

The dataset therefore contains a combination of numerical and categorical
property features.

---

## 6. SalePrice Distribution

The `SalePrice` distribution was inspected before modeling.

Calculated skewness:

`1.8828757597682129`

This showed that house prices were strongly right-skewed.

Most observations were concentrated in the lower and middle price ranges,
while a smaller number of expensive houses formed a long right tail.

This observation later helped explain why several of the largest model errors
occurred for expensive properties.

---

## 7. Missing-Value Investigation

Missing values were not immediately treated as generic missing data.

Several variables were investigated together with related property features.

Examples included:

- Missing `PoolQC` values corresponded to houses with `PoolArea = 0`
- Missing `GarageType` values corresponded to houses with `GarageCars = 0`
- Missing `BsmtQual` values corresponded to houses with `TotalBsmtSF = 0`

This showed that many missing values represented structural absence:

- no pool
- no garage
- no basement

rather than accidental data loss.

---

## 8. Pandas Missing-Value Parsing

The raw CSV was also loaded using:

```python
pd.read_csv("../data/train.csv", keep_default_na=False)

```markdown
This revealed an important parsing issue.

For example, the raw `MasVnrType` values included:

- `None`: 864
- `BrkFace`: 445
- `Stone`: 128
- `BrkCmn`: 15
- `NA`: 8

With Pandas' default parsing behavior, values such as `"None"` and `"NA"` could
be interpreted as missing values.

This investigation showed why the meaning of missing data needed to be checked
before applying preprocessing.

The cleaning strategy therefore attempted to preserve domain meaning instead
of blindly applying one generic imputation rule.

---

## 9. Exploratory Data Analysis

The numerical features most strongly correlated with `SalePrice` included:

| Feature | Correlation |
|---|---:|
| OverallQual | 0.790982 |
| GrLivArea | 0.708624 |
| GarageCars | 0.640409 |
| GarageArea | 0.623431 |
| TotalBsmtSF | 0.613581 |
| 1stFlrSF | 0.605852 |
| FullBath | 0.560664 |
| TotRmsAbvGrd | 0.533723 |
| YearBuilt | 0.522897 |
| YearRemodAdd | 0.507101 |

`OverallQual` and `GrLivArea` showed the strongest numerical relationships
with house prices.

These results suggest that overall property quality and usable living space
are particularly important predictors of sale price.

---

## 10. Data Preparation

The preprocessing workflow separated numerical and categorical variables.

Numerical preprocessing included:

- missing-value imputation
- scaling where appropriate

Categorical preprocessing included:

- domain-aware missing-value handling
- missing-value imputation where necessary
- one-hot encoding

Scikit-learn `Pipeline` and `ColumnTransformer` were used to create a reusable
and reproducible preprocessing workflow.

The dataset was divided into training and validation sets using a fixed random
state for reproducibility.

---

## 11. Models Evaluated

Four regression approaches were compared:

1. Dummy Regressor
2. Ridge Regression
3. Random Forest Regressor
4. Gradient Boosting Regressor

The Dummy Regressor provided a simple baseline so that the machine-learning
models could be compared against a naive prediction strategy.

---

## 12. Model Comparison

The final validation results showed that Gradient Boosting achieved the best
performance among the tested models.

Approximate results were:

| Model | RMSE | MAE | R² |
|---|---:|---:|---:|
| Gradient Boosting | $27,790 | $17,165 | 0.899 |
| Random Forest | $29,024 | — | — |
| Ridge Regression | $29,721 | — | — |
| Dummy Baseline | $87,619 | — | — |

Gradient Boosting substantially outperformed the Dummy baseline.

The final Gradient Boosting validation performance was approximately:

- RMSE: $27,790
- MAE: $17,165
- R²: 0.899

This suggests that the model captured a large portion of the variation in
house prices and produced substantially better predictions than the simple
baseline. fileciteturn19file1

---

## 13. Cross-Validation

To verify that the Gradient Boosting result was not caused by one favorable
train-validation split, the model was evaluated using 5-fold cross-validation.

The RMSE values were:

- $23,534.66
- $32,806.17
- $27,905.74
- $22,541.65
- $27,567.98

The mean cross-validation RMSE was:

**$26,871.24**

The standard deviation was:

**$3,651.22**

The mean cross-validation RMSE was close to the original validation RMSE of
approximately $27,790.

This provides additional evidence that the model performs reasonably
consistently across different subsets of the dataset. fileciteturn18file0

---

## 14. Prediction Error Analysis

The Gradient Boosting model performed well overall, but some individual
properties produced large prediction errors.

One example was:

- Actual price: approximately $611,657
- Predicted price: approximately $403,266
- Underprediction: more than $200,000

Other large errors also appeared among relatively expensive homes.

There were also some large overpredictions for mid-priced homes.

These results suggest that unusual or expensive properties may contain
characteristics that are more difficult for the model to capture.

This is also consistent with the right-skewed `SalePrice` distribution
observed earlier.

Therefore, strong overall RMSE and R² results do not guarantee that every
individual house prediction will be accurate. fileciteturn20file1

---

## 15. Feature Importance

The Gradient Boosting model identified several important predictive features.

The strongest features included:

- `OverallQual` — approximately 50.2%
- `GrLivArea` — approximately 15.4%
- `GarageCars` — approximately 4.2%
- `TotalBsmtSF` — approximately 3.5%
- `BsmtFinSF1` — approximately 3.3%

`OverallQual` was the most important feature by a large margin.

`GrLivArea` was the second most important feature.

This result was consistent with the earlier correlation analysis, where
`OverallQual` and `GrLivArea` also showed the strongest relationships with
`SalePrice`.

Feature importance reflects how the model uses variables for prediction and
should not be interpreted as proving a causal relationship. fileciteturn20file3

---

## 16. Generated Results

The project generated the following result files:

- `model_comparison.csv`
- `cross_validation_rmse.csv`
- `prediction_errors.csv`
- `feature_importance.csv`

The project also generated the following figures:

- `saleprice_distribution.png`
- `missing_values.png`
- `top_correlations.png`
- `actual_vs_predicted.png`
- `feature_importance.png`

These artifacts were stored in the `results/` and `figures/` directories and
were generated from the final notebook workflow. fileciteturn18file4

---

## 17. Notebook Reproducibility

After experimentation, the notebook was cleaned and prepared for final
validation.

Temporary tests, failed cells, and unnecessary notebook content were reviewed.

The final workflow used:

`Restart Kernel → Run All → Save`

The notebook file was also inspected programmatically to verify that code
cells had been executed.

The purpose of this step was to make sure that the reported results could be
reproduced from the notebook rather than depending on a specific interactive
execution order. fileciteturn20file4

---

## 18. GitHub Validation

The rebuilt Assignment 1 project was committed and pushed to GitHub.

The final working directory included:

- planning documents
- dataset
- executed Jupyter notebook
- figures
- CSV result files
- chat transcript directory
- README documentation

The local Python `.venv` was intentionally excluded from Git.

Older Assignment 1 directories were preserved only as backups.

---

## 19. Role of AI and Human Validation

The AI assistant supported:

- project planning
- project organization
- Python environment troubleshooting
- code generation
- debugging
- exploratory data analysis
- preprocessing design
- model comparison
- cross-validation
- prediction-error analysis
- feature interpretation
- documentation

However, AI output was not accepted blindly.

The code was executed locally, unexpected behavior was investigated, and the
final interpretations were based on the actual notebook outputs.

The missing-value investigation was an important example.

Instead of immediately applying generic imputation, the meaning of `"NA"`,
`"None"`, and structural missing values was investigated before the cleaning
strategy was finalized.

This demonstrated that AI-assisted data science still requires human
validation, domain interpretation, and reproducibility checks.

---

## Final Summary

The September 6 session rebuilt Part 1 as a complete AI-assisted data science
workflow:

Requirements  
→ Intent  
→ Specification  
→ Plan  
→ Environment Setup  
→ Data Understanding  
→ Missing-Value Investigation  
→ Exploratory Data Analysis  
→ Data Preparation  
→ Baseline Modeling  
→ Model Comparison  
→ Cross-Validation  
→ Prediction Error Analysis  
→ Feature Importance  
→ Artifact Generation  
→ Reproducibility Validation  
→ GitHub Documentation

The strongest model was Gradient Boosting with approximately:

- RMSE: $27,790
- MAE: $17,165
- R²: 0.899

The 5-fold cross-validation mean RMSE was approximately:

- $26,871

The strongest predictive features were:

- `OverallQual`
- `GrLivArea`

The project demonstrated both the usefulness of AI-assisted development and
the importance of human verification throughout the data science workflow.
