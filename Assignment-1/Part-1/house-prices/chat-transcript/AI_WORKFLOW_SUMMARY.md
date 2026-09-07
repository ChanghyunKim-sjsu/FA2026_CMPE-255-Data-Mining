# AI-Assisted Workflow Summary

## CMPE 255 Assignment 1 - Part 1: House Prices

This document is an English guide to the AI-assisted work recorded in the
original ChatGPT transcript for Part 1. It summarizes the workflow; it does not
replace, translate, or reconstruct the original conversation. The original
export is preserved separately as `original_chat_transcript.pdf`. Any Korean
interface or progress text in that export remains unchanged.

## Project Objective

The project used the Kaggle **House Prices: Advanced Regression Techniques**
dataset to study an end-to-end regression problem: predicting a home's
`SalePrice` from its physical characteristics, quality, location, and related
attributes. The work was organized with the CRISP-DM methodology so that the
conversation documented not only model training, but also problem definition,
data investigation, preparation, evaluation, interpretation, and communication.

## How AI Assisted the Work

ChatGPT supported the project by:

- recommending a suitable dataset and progressive modeling strategy;
- breaking the analysis into CRISP-DM phases and smaller tasks;
- proposing Python analyses, visualizations, preprocessing, and model code;
- explaining statistical and machine-learning concepts in plain language;
- comparing model results against the chosen evaluation criteria;
- identifying limitations and helping organize a report-ready narrative.

The conversation deliberately compared simple and more complex approaches
rather than assuming that the most complex model would perform best.

## CRISP-DM Workflow

### 1. Business Understanding

The analysis defined the task as supervised regression with `SalePrice` as the
target. It considered both practical dollar error and Kaggle-style logarithmic
error. This led to the use of RMSE, MAE, R-squared, and RMSLE, with RMSLE treated
as the primary selection metric for the final model.

### 2. Data Understanding

The dataset inspection covered 1,460 observations and 81 columns, including 79
explanatory variables, the `Id` field, and the target. The workflow examined:

- data types, duplicate rows, and target completeness;
- the strongly right-skewed `SalePrice` distribution;
- numerical correlations with sale price;
- categorical relationships such as neighborhood and quality ratings;
- missing-value patterns and their domain meanings;
- unusually large or expensive homes that could be difficult to predict.

The analysis found that `OverallQual` and `GrLivArea` had especially strong
relationships with `SalePrice`. It also highlighted meaningful neighborhood
price differences and treated unusual records as cases to investigate rather
than automatically delete.

### 3. Data Preparation

The preparation process removed `Id` as a non-predictive identifier and used an
80/20 training-validation split with `random_state=42`. Numerical variables
were median-imputed. Categorical variables received an explicit `Missing`
category and were one-hot encoded with unknown categories ignored. The skewed
target was transformed with `log1p` for models where that representation was
appropriate, and predictions were transformed back to dollar values for
interpretation.

These steps were designed to keep preprocessing reproducible and to avoid
learning preprocessing decisions from the validation data.

### 4. Modeling

The transcript records a progression through five approaches:

1. Median-price baseline
2. Log-target linear regression
3. Random forest regression
4. Gradient boosting regression
5. A small neural-network experiment

This progression established a meaningful baseline, tested linear and nonlinear
relationships, and provided evidence that added model complexity does not
automatically improve tabular-data performance.

### 5. Evaluation and Interpretation

In the recorded holdout results, log-linear regression achieved the lowest RMSE
and highest R-squared, while gradient boosting achieved the lowest RMSLE
(approximately 0.130 versus 0.132 for log-linear regression). Because RMSLE was
the selected primary metric, gradient boosting was chosen as the final model in
the transcript. Three-fold cross-validation also favored gradient boosting,
with a recorded mean RMSLE of approximately `0.138 +/- 0.016`.

Prediction-error analysis showed that typical homes were estimated more
accurately than unusually expensive homes, which the model tended to
underpredict. Feature-importance analysis identified overall quality and
above-ground living area as the leading predictors, consistent with the earlier
exploratory analysis. The conversation explicitly distinguished predictive
importance from causal effect.

### 6. Communication

The final discussion converted the technical findings into a concise story:

- overall quality and usable living space were the strongest recurring signals;
- neighborhood, age, basement size, garage capacity, and other quality measures
  also contributed;
- transforming a skewed target allowed a simple linear model to remain highly
  competitive;
- a small neural network did not outperform the strongest traditional models;
- expensive and unusual homes were the hardest cases to predict;
- results from Ames, Iowa should not be generalized to every housing market.

For this assignment, the CRISP-DM deployment phase was interpreted as clear
communication through the notebook, figures, repository documentation, and
planned video walkthrough rather than production deployment of a live model.

## Human Review and Reproducibility Note

The original conversation is evidence of the AI-assisted analytical process,
not a guarantee that every preserved result file was generated by one identical
environment. A later local audit reran a corrected script and confirmed the
overall workflow, but some holdout metrics differed from the legacy transcript,
and the preserved notebook does not contain the neural-network experiment or
saved execution outputs. The repository documents those differences in
`results/README.md`.

Accordingly, the transcript's metrics should be described as **recorded results**
until the final notebook, tables, and figures are regenerated from one controlled
end-to-end run. This disclosure preserves the distinction between AI-generated
guidance, executed evidence, and the student's final interpretation.

## Transcript Provenance

`original_chat_transcript.pdf` is a byte-for-byte copy of the existing 61-page
ChatGPT Exporter file for the Part 1 House Prices conversation. The source file
shows the original ChatGPT conversation URL and spans from the initial dataset
and model-selection discussion through the final CRISP-DM conclusions. No
messages were translated, rewritten, or synthesized for that PDF.
