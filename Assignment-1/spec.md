# Specification - Assignment 1

> Supplemental agentic-workflow document added for organization; not a professor-required file.

## Submission structure

The assignment root contains one overview README, one artifact audit, one TODO tracker, and two clearly separated parts. Each completed experiment should contain:

- a focused README;
- source or access instructions for its dataset;
- an executable notebook and/or script;
- saved outputs that prove execution;
- result tables and figures generated from the same final run;
- the prompt or chat evidence used with the AI assistant;
- a report or concise written interpretation;
- a working YouTube link at the assignment root.

## Part 1 analytical specification

**Problem:** supervised regression of `SalePrice` from the Kaggle House Prices training data.  
**Framework:** CRISP-DM.  
**Core stages:** business understanding, data understanding, preparation, modeling, evaluation, and communication.  
**Models recorded in the transcript:** median baseline, log-linear regression, random forest, gradient boosting, and an optional small neural network.  
**Metrics:** RMSE, MAE, R2, RMSLE, and cross-validation RMSLE.  
**Interpretation:** feature influence, error behavior, limitations, and the effect of metric choice on model selection.

## Part 2 replication specification

| Experiment | Core method | Minimum evidence required |
|---|---|---|
| Customer segmentation | Scaling, K-Means, elbow/silhouette comparison, PCA, cluster interpretation | Executed notebook/script, dataset, k-selection results, figures, segment table, prompt/chat evidence |
| Market basket analysis | Transaction preparation, frequent itemsets, association rules, support/confidence/lift interpretation | Executed notebook/script, dataset, rule table, figures, prompt/chat evidence |
| Anomaly detection | Isolation Forest and LOF comparison with suitable anomaly metrics | Executed notebook/script, dataset, evaluation table, figures, prompt/chat evidence |

## Acceptance criteria

- No file in `Assignment1/` changes during reorganization.
- Every retained legacy artifact appears in `ARTIFACT_AUDIT.md` with KEEP or REVISE status.
- Placeholder-only legacy files marked DISCARD remain in the backup but are not promoted into the submission structure.
- All internal Markdown links resolve.
- All Part 2 titles use "Assignment 1 - Part 2" consistently.
- Notebook status is determined from saved notebook metadata and outputs, not appearance or memory.
- README claims match the files actually present.
- YouTube URLs and final public access are checked immediately before submission.
