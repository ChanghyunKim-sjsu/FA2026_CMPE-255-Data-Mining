# Part 1 - House Prices End-to-End Data Science

## Objective

Use an AI assistant and the CRISP-DM framework to understand the Kaggle House Prices dataset, prepare mixed numerical and categorical data, compare regression approaches, evaluate them with appropriate metrics, and translate the result into an understandable story.

## Dataset verification

The included [`data/train.csv`](./data/train.csv) was checked on September 6, 2026:

- 1,460 rows and 81 columns;
- 1,460 unique `Id` values;
- zero duplicate rows;
- zero missing `SalePrice` values;
- `SalePrice` range: $34,900 to $755,000.

Dataset source: [Kaggle House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques).

## End-to-end journey

The [61-page AI conversation export](./chat-transcript/house-prices-chat-transcript.pdf) records the following sequence:

1. **Business understanding:** define a residential sale-price regression problem and technical/analytical success criteria.
2. **Data understanding:** inspect shape, variable types, target distribution, missingness, correlations, neighborhoods, and unusual houses.
3. **Data preparation:** remove `Id`, impute numerical features with medians, represent missing categorical values explicitly, one-hot encode categories, and split training from validation data.
4. **Modeling:** establish a median baseline, then compare log-linear regression, random forest, gradient boosting, and a small neural-network experiment.
5. **Evaluation:** compare dollar error and logarithmic error, use three-fold cross-validation, inspect where the final model struggles, and review feature importance.
6. **Communication:** summarize findings, limitations, and the practical meaning of the output.

## Recorded results and provenance warning

The legacy transcript records the following holdout values:

| Model | RMSE | MAE | R2 | RMSLE |
|---|---:|---:|---:|---:|
| Median baseline | 88,667 | 59,568 | -0.025 | 0.432 |
| Log-linear regression | 22,902 | 15,076 | 0.932 | 0.132 |
| Random forest | 29,007 | 17,469 | 0.890 | 0.152 |
| Gradient boosting | 28,787 | 16,763 | 0.892 | 0.130 |
| Small neural network | 34,646 | 22,312 | 0.844 | 0.172 |

The preserved `model_metrics.csv` and model-comparison PNG do **not** fully match that table: both show random-forest validation RMSLE as `0.148`, which is the recorded random-forest cross-validation mean, and the CSV omits the neural-network row. The current notebook also has no saved outputs. These files are retained for auditability, not treated as final authoritative results.

See [`results/README.md`](./results/README.md) for the independent rerun and reconciliation TODO.

## Interpretation in plain language

Overall construction quality and above-ground living space emerged as the strongest predictors. Neighborhood, age, basement area, garage capacity, and other quality-related features also contributed. Log-linear regression produced the lowest recorded dollar error, while gradient boosting produced the lowest recorded RMSLE and the best average cross-validation RMSLE. This illustrates why a model should be selected against the metric that matches the problem rather than by a vague claim that one model is universally best.

The analysis also showed a limitation: expensive and unusual homes were harder to predict. Feature importance describes predictive usefulness, not causation, and the Ames, Iowa data should not be treated as a universal housing market model.

## Artifacts

- [`notebooks/house_prices_analysis.ipynb`](./notebooks/house_prices_analysis.ipynb) - preserved summary notebook; **TODO: execute and save all outputs**.
- [`src/house_prices_analysis.py`](./src/house_prices_analysis.py) - corrected runnable version of the legacy script.
- [`figures/recorded/`](./figures/recorded/) - six figures preserved from the prior analysis, with known caveats documented in the audit.
- [`results/recorded/`](./results/recorded/) - preserved legacy CSV result records.
- [`chat-transcript/house-prices-chat-transcript.pdf`](./chat-transcript/house-prices-chat-transcript.pdf) - complete Part 1 ChatGPT export.
- [`report/README.md`](./report/README.md) - report status and TODO.
- [`requirements.txt`](./requirements.txt) - package versions used for the independent verification run.

## Run the script

From this directory:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/house_prices_analysis.py
```

Package and platform changes can affect exact metrics. Do not overwrite `results/recorded/`; write final, freshly generated evidence into a separate results location after reconciling the pipeline.

## Video

`TODO: ADD_PART_1_YOUTUBE_URL`

Medium publishing is intentionally omitted because the professor said it is not required.
