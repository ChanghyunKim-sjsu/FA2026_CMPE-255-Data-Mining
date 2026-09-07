# Part 1 — Implementation Plan

## Phase 1 — Project Setup

- [ ] Confirm the House Prices dataset is available
- [ ] Place the dataset in the `data/` directory
- [ ] Create the final Jupyter notebook
- [ ] Confirm the Python environment and required packages
- [ ] Record the initial project structure in GitHub

---

## Phase 2 — Data Understanding

- [ ] Load `train.csv`
- [ ] Inspect the first rows
- [ ] Check dataset shape
- [ ] Inspect column names and data types
- [ ] Count numerical and categorical features
- [ ] Check duplicate rows
- [ ] Check missing values
- [ ] Inspect `SalePrice` summary statistics
- [ ] Summarize the initial findings in my own words

---

## Phase 3 — Exploratory Data Analysis

- [ ] Plot the `SalePrice` distribution
- [ ] Investigate whether the target is skewed
- [ ] Analyze missing-value patterns
- [ ] Examine numerical correlations with `SalePrice`
- [ ] Investigate important candidate features
- [ ] Inspect potential outliers
- [ ] Save useful figures to the `figures/` directory
- [ ] Write a short interpretation after each important visualization

Initial relationships to investigate may include:

- `OverallQual` vs `SalePrice`
- `GrLivArea` vs `SalePrice`
- `GarageCars` vs `SalePrice`
- `TotalBsmtSF` vs `SalePrice`
- `YearBuilt` vs `SalePrice`

These may change depending on the actual EDA findings.

---

## Phase 4 — Data Preparation

- [ ] Separate features (`X`) and target (`y`)
- [ ] Create training and validation splits
- [ ] Identify numerical columns
- [ ] Identify categorical columns
- [ ] Build numerical missing-value preprocessing
- [ ] Build categorical missing-value preprocessing
- [ ] Encode categorical variables
- [ ] Apply scaling only when justified by the model
- [ ] Combine preprocessing with `ColumnTransformer`
- [ ] Verify the preprocessing pipeline runs successfully

The preprocessing pipeline should be fit only on training data to reduce
data leakage.

---

## Phase 5 — Baseline Model

- [ ] Train a `DummyRegressor`
- [ ] Generate validation predictions
- [ ] Calculate RMSE
- [ ] Calculate MAE
- [ ] Calculate R² if useful
- [ ] Save the baseline results

The baseline will provide a reference point for judging whether the machine
learning models provide meaningful improvement.

---

## Phase 6 — Candidate Models

Evaluate multiple regression models.

### Model 1 — Linear / Regularized Linear Model

- [ ] Train the model
- [ ] Generate validation predictions
- [ ] Calculate evaluation metrics
- [ ] Record the results

### Model 2 — Random Forest Regressor

- [ ] Train the model
- [ ] Generate validation predictions
- [ ] Calculate evaluation metrics
- [ ] Record the results

### Model 3 — Gradient Boosting Regressor

- [ ] Train the model
- [ ] Generate validation predictions
- [ ] Calculate evaluation metrics
- [ ] Record the results

Additional models should only be added if there is a clear reason.

---

## Phase 7 — Model Comparison

- [ ] Combine model metrics into a comparison table
- [ ] Compare RMSE
- [ ] Compare MAE
- [ ] Compare R² if reported
- [ ] Compare all models against the baseline
- [ ] Consider cross-validation for stronger validation
- [ ] Select the final model
- [ ] Explain why the final model was selected

The final model should not be selected only because it is the most complex.

---

## Phase 8 — Model Interpretation

- [ ] Create predicted vs actual visualization
- [ ] Calculate prediction errors
- [ ] Inspect the largest errors
- [ ] Identify major underpredictions
- [ ] Identify major overpredictions
- [ ] Investigate important predictive features when supported by the model
- [ ] Discuss potential explanations for the observed errors
- [ ] Document model limitations

---

## Phase 9 — Final Validation

Before using any result in the final submission:

- [ ] Restart the notebook kernel
- [ ] Run all notebook cells from top to bottom
- [ ] Confirm that no cell fails
- [ ] Confirm reported metrics match notebook output
- [ ] Confirm figures match the final run
- [ ] Confirm random states are fixed where appropriate
- [ ] Remove unused experimental code
- [ ] Remove misleading or outdated results

Only the results from this final successful run will be treated as the
official project results.

---

## Phase 10 — Documentation

- [ ] Update the Part 1 README
- [ ] Describe the business problem
- [ ] Describe the dataset
- [ ] Explain the workflow
- [ ] Include final model comparison
- [ ] Include important visualizations
- [ ] Explain results in my own words
- [ ] Document limitations
- [ ] Add instructions for reproducing the analysis
- [ ] Record AI-assisted workflow artifacts

---

## Phase 11 — Assignment Deliverables

- [ ] Confirm all Part 1 artifacts are in GitHub
- [ ] Export or save the AI conversation transcript
- [ ] Confirm the GitHub repository is publicly viewable
- [ ] Record the Part 1 YouTube walkthrough
- [ ] Explain the end-to-end journey in the video
- [ ] Paraphrase and explain the results rather than reading AI output
- [ ] Add the YouTube URL to the README
- [ ] Perform a final professor-requirement checklist

Medium publication is not required.
