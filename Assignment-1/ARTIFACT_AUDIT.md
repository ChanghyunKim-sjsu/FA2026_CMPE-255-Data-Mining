# Existing `Assignment1` Artifact Audit

Audit date: September 6, 2026  
Source audited: [`../Assignment1/`](../Assignment1/) on the `main` branch

Classification meanings:

- **KEEP** - useful and sufficiently accurate to preserve in the new structure.
- **REVISE** - useful, but requires correction, stronger provenance, rerunning, or clearer labeling.
- **DISCARD** - not copied into the new structure because it adds no submission value. The original remains in the untouched backup.

| Existing file | Decision | Reason and action in `Assignment-1` |
|---|---|---|
| `Assignment1/Chat_transcript.pdf` | KEEP | Valid, readable 61-page ChatGPT export covering House Prices planning, CRISP-DM, analysis, modeling, evaluation, and interpretation. Copied with a descriptive name under `Part-1/house-prices/chat-transcript/`. |
| `Assignment1/README.md` | REVISE | Strong Part 1 narrative, but it incorrectly says `train.csv` and the transcript are absent, uses inconsistent lowercase paths, lists Medium, omits Part 2, and does not flag the unexecuted notebook. Replaced by layered root and Part 1 READMEs. |
| `Assignment1/data/train.csv` | KEEP | Valid House Prices training data: 1,460 rows, 81 columns, 1,460 unique IDs, no duplicate rows, and no missing target values. Copied unchanged. |
| `Assignment1/images/cross_validation_rmsle.png` | KEEP | Legible and consistent with the cross-validation values recorded in the transcript. Preserved as a recorded figure. |
| `Assignment1/images/eda_summary.png` | REVISE | Core statistics are consistent with the dataset, but the footer says row-level data was unavailable even though `train.csv` is included. Preserved only as a clearly labeled recorded/legacy figure. |
| `Assignment1/images/feature_importance_summary.png` | KEEP | Clearly limits the chart to the two exact importance values preserved from the prior run. Retained with provenance caveat. |
| `Assignment1/images/key_findings_summary.png` | KEEP | Readable summary of the recorded Part 1 conclusions. |
| `Assignment1/images/missing_values_summary.png` | KEEP | Readable and consistent with the transcript's missing-value interpretation. |
| `Assignment1/images/model_metrics_comparison.png` | REVISE | The random-forest RMSLE is shown as `0.148`, but the transcript records `0.152` for validation and `0.148` for cross-validation. Preserved only as a legacy figure and not used as authoritative evidence. |
| `Assignment1/links/youtube_links.md` | DISCARD | Contains only a placeholder already duplicated in the README. Not copied; corrected placeholders are centralized in the new root README. |
| `Assignment1/notebooks/house_prices_analysis.ipynb` | REVISE | Summary notebook with five code cells, all unexecuted, and no saved outputs; data loading is commented out. Copied for recovery, but explicitly marked TODO and not presented as executed evidence. |
| `Assignment1/requirements.txt` | REVISE | Lists the correct core packages but has no versions, so reruns can drift. The new copy pins the versions used for the September 6 verification run. |
| `Assignment1/results/cross_validation_results.csv` | KEEP | Matches the values recorded in the ChatGPT transcript. Preserved under `results/recorded/`; only Gradient Boosting has been independently rerun with the current script. |
| `Assignment1/results/feature_importance_summary.csv` | KEEP | Transparently distinguishes two approximate numeric values from factors without preserved values. Retained as a recorded result, not a newly reproduced result. |
| `Assignment1/results/model_metrics.csv` | REVISE | Omits the neural-network row recorded in the transcript, assigns random forest's cross-validation RMSLE to its validation row, and does not match the current environment's rerun. Preserved as legacy evidence with a warning. |
| `Assignment1/src/house_prices_analysis.py` | REVISE | Runnable core workflow, but its documentation claimed it wrote CSVs when it did not, contained an unused pipeline, and used default Gradient Boosting settings inconsistent with the transcript. The copied script was corrected without modifying the backup. |

## Audit conclusion

The old folder is a useful **Part 1 backup**, not a complete Assignment 1 submission. It has no Part 2 artifacts, no working YouTube URL, no finished standalone report, and no executed end-to-end notebook. The new structure preserves everything useful while exposing these gaps as TODOs instead of hiding or fabricating them.
