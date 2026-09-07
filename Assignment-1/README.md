# Assignment 1 - AI-Assisted Data Science

> **Submission status: in progress.** The House Prices materials have been reorganized and audited. The three Part 2 experiment folders are present, but their previously created notebooks, code, datasets, figures, and result files were not found in the GitHub repository and still need to be restored. YouTube links are also pending.

This directory brings both assignment parts into one clear submission structure:

- **Part 1:** an AI-assisted, end-to-end data science project using Kaggle's [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) dataset.
- **Part 2:** replications of three representative experiments from the professor's [`data_science_examples`](https://github.com/dlmastery/data_science_examples) repository: customer segmentation, market basket analysis, and anomaly detection.

The original [`Assignment1/`](../Assignment1/) directory has not been edited or deleted. It remains a backup until this structure is fully verified.

## Professor requirements and current status

| Requirement | Part | Status | Evidence / next action |
|---|---|---:|---|
| Use a popular Kaggle dataset | 1 | Complete | House Prices training data is included. |
| Use an agentic coding assistant or chatbot | 1 | Complete | The exported ChatGPT transcript is included. |
| Show an end-to-end data science workflow | 1 | Partial | CRISP-DM narrative, data, script, figures, and recorded results are present; the notebook is a summary notebook with no saved execution output. |
| Organize all artifacts in GitHub with a clear README | 1 and 2 | Partial | This directory provides the organization; Part 2 artifacts still need recovery. |
| Export the AI chat transcript | 1 | Complete | [House Prices chat transcript](./Part-1/house-prices/chat-transcript/house-prices-chat-transcript.pdf). |
| Replicate professor experiments using the supplied prompts | 2 | Partial | Three experiment scopes and source prompts are documented; the prior implementation artifacts are missing from the audited repository. |
| Explain and paraphrase the results in the student's own words | 1 and 2 | Partial | Part 1 interpretation is below. Part 2 interpretations must be verified after artifacts are restored and rerun. |
| Publish the repository with public-view permission | 1 and 2 | Verified for current repository | Anonymous HTTPS cloning succeeded before the reorganization, and an unauthenticated remote lookup confirmed the new `main` commit after the push on September 6, 2026. Recheck after future final-artifact pushes. |
| Upload YouTube walkthrough(s) and link them from the README | 1 and 2 | TODO | Replace the placeholders below with public or unlisted YouTube URLs. |
| Publish on Medium | - | Not required | Omitted because the professor said Medium publishing is not required. |

## Repository map

```text
Assignment-1/
├── README.md
├── ARTIFACT_AUDIT.md
├── TODO.md
├── intent.md
├── spec.md
├── plan.md
├── Part-1/
│   └── house-prices/
│       ├── README.md
│       ├── requirements.txt
│       ├── data/
│       ├── notebooks/
│       ├── src/
│       ├── figures/recorded/
│       ├── results/recorded/
│       ├── chat-transcript/
│       └── report/
└── Part-2/
    ├── README.md
    ├── customer-segmentation/
    ├── market-basket-analysis/
    ├── anomaly-detection/
    ├── chat-transcript/
    └── video/
```

The `intent.md`, `spec.md`, and `plan.md` files are **supplemental agentic-workflow documentation added by the student for organization**. They are not presented as professor-required deliverables.

## Part 1 - House Prices

The analysis follows the CRISP-DM story:

1. Define the business and prediction question.
2. Inspect the 1,460-row, 81-column training dataset.
3. Explore price distribution, missing values, numerical relationships, categorical relationships, and unusual observations.
4. Prepare numerical and categorical features without leaking validation data into training.
5. Compare a median baseline, log-linear regression, random forest, gradient boosting, and an optional neural-network experiment recorded in the transcript.
6. Evaluate the models with RMSE, MAE, R2, RMSLE, and cross-validation.
7. Translate the findings into plain language, limitations, and a video-ready narrative.

### Student-ready paraphrase

The analysis suggests that construction quality and usable living area carry the strongest predictive signal, while neighborhood, age, basement space, garage capacity, and other quality-related features also matter. The important modeling lesson is that the winning model depends on the evaluation goal: log-linear regression was strongest on dollar-based error in the original transcript, while gradient boosting was chosen because it performed best on the Kaggle-style logarithmic error and remained strongest in the recorded cross-validation comparison. The model was more reliable for typical homes than for unusually expensive properties, so these results should not be interpreted as causal or universal pricing rules.

See the [Part 1 README](./Part-1/house-prices/README.md) for artifact provenance, recorded metrics, and reproducibility cautions.

## Part 2 - Professor experiment replications

The selected replication set is:

1. [Customer Segmentation](./Part-2/customer-segmentation/README.md)
2. [Market Basket Analysis](./Part-2/market-basket-analysis/README.md)
3. [Anomaly Detection](./Part-2/anomaly-detection/README.md)

The assignment wording does not state an exact number of experiments. These three were previously selected as representative replications. The audited repository contains none of the earlier Part 2 implementation files, so the folders document their provenance and recovery requirements without inventing missing outputs.

## YouTube walkthroughs

- **Assignment 1 - Part 1: House Prices:** `TODO: ADD_PART_1_YOUTUBE_URL`
- **Assignment 1 - Part 2: Experiment Replications:** `TODO: ADD_PART_2_YOUTUBE_URL`

Use **"Assignment 1 - Part 2"** as the Part 2 recording title. A corrected [walkthrough outline](./Part-2/video/WALKTHROUGH_OUTLINE.md) is included.

## Before submission

Work through the critical items in [`TODO.md`](./TODO.md), then verify that every README link opens on GitHub, every submitted notebook shows saved outputs, both YouTube URLs work without private access, and the repository remains publicly viewable.
