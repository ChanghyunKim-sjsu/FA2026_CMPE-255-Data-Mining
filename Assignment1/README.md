# Assignment 1 - House Prices Data Science Project

## Project Overview

This project analyzes the Kaggle **House Prices: Advanced Regression Techniques** dataset using ChatGPT as an AI-assisted data science tool.

The goal of the project was to understand the housing dataset, perform exploratory data analysis, preprocess the data, train multiple regression models, compare their performance, and identify the most important factors affecting house prices.

The workflow was completed interactively with ChatGPT, including code generation, explanations, result interpretation, and model comparison.

## Dataset

**Dataset:** Kaggle House Prices: Advanced Regression Techniques  
**Target Variable:** `SalePrice`

The training dataset used in the analysis contains:

- 1,460 rows
- 81 columns
- Numerical and categorical housing features
- Housing characteristics such as quality, size, neighborhood, garage information, basement information, and year built

The objective is to predict the final sale price of each house.

The Kaggle `train.csv` file is not included in this package. To rerun the notebook or Python script, download it from Kaggle and place it at:

```text
assignment1/data/train.csv
```

## Data Science Workflow

1. Dataset understanding
2. Data quality inspection
3. Exploratory data analysis
4. Missing value analysis
5. Feature preprocessing
6. Train-validation split
7. Baseline model creation
8. Machine learning model training
9. Model evaluation
10. Cross-validation
11. Feature importance analysis
12. Final interpretation

## Exploratory Data Analysis

### Sale Price Distribution

The average house sale price was approximately **$180,921**.

The median house sale price was approximately **$163,000**.

The target variable was positively skewed, with a skewness of approximately **1.88**. This means that most houses were concentrated in the lower and middle price ranges, while a smaller number of expensive houses created a long right tail.

### Important Relationships

Several features showed strong relationships with house prices:

- `OverallQual` and `SalePrice`: correlation approximately **0.791**
- `GrLivArea` and `SalePrice`: correlation approximately **0.709**
- Median sale prices across neighborhoods ranged approximately from **$88,000 to $315,000**

These results suggest that overall quality, living area, and location were major drivers of house prices.

## Missing Value Analysis

Several variables contained large numbers of missing values, including:

- `PoolQC`
- `MiscFeature`
- `Alley`
- `Fence`
- `FireplaceQu`

Some missing values represent the absence of a feature rather than bad data. For example, a missing `PoolQC` value may simply mean that the house does not have a pool.

For this reason, missing categorical values were generally represented using a separate `"Missing"` category instead of deleting those rows or columns.

## Data Preprocessing

The preprocessing steps included:

- Removed the `Id` column
- Used median imputation for missing numerical values
- Replaced missing categorical values with `"Missing"`
- Applied one-hot encoding to categorical variables
- Created approximately **301 final model features**
- Used an **80/20 train-validation split**
- Used `random_state=42` for reproducibility

## Models Evaluated

| Model | RMSE | MAE | R2 | RMSLE |
|---|---:|---:|---:|---:|
| Median Baseline | $88,667 | $59,568 | -0.025 | 0.432 |
| Log Linear Regression | $22,902 | $15,076 | 0.932 | 0.132 |
| Random Forest | $29,007 | $17,469 | 0.890 | ~0.148 |
| Gradient Boosting | $28,787 | $16,763 | 0.892 | **0.130** |

The Log Linear Regression model achieved the best RMSE, MAE, and R2 scores on the validation set.

However, the **Gradient Boosting model achieved the best RMSLE score of approximately 0.130**. RMSLE is especially useful for this type of housing-price problem because it measures relative prediction error and reduces the effect of very expensive houses.

Because the Kaggle House Prices competition commonly uses RMSLE-style evaluation, Gradient Boosting was selected as the final model.

## Cross-Validation Results

Three-fold cross-validation was used to evaluate whether model performance was stable across different subsets of the training data.

| Model | Mean RMSLE | Standard Deviation |
|---|---:|---:|
| Gradient Boosting | **0.138** | 0.016 |
| Random Forest | 0.148 | 0.019 |
| Log Linear Regression | 0.159 | 0.028 |

Gradient Boosting achieved the best average cross-validation RMSLE, supporting the final model selection.

## Feature Importance

The Gradient Boosting model showed that a small number of features contributed heavily to the predictions.

The two most important features were:

- `OverallQual`: approximately **46%**
- `GrLivArea`: approximately **17%**

Other influential factors included:

- House age
- Basement size
- Garage capacity
- Construction quality
- Neighborhood
- Additional size and quality-related features

Overall, the results suggest that house prices are strongly influenced by **quality, usable living space, location, property age, and supporting amenities**.

## Key Findings

- Overall house quality was the strongest predictor of sale price.
- Larger above-ground living areas were generally associated with higher prices.
- Neighborhood location had a significant effect on house value.
- Missing values sometimes carried real-world meaning and should not always be treated as bad data.
- A simple baseline model performed poorly, confirming that the dataset contained useful predictive information.
- Multiple models performed well, but Gradient Boosting achieved the best RMSLE.
- Cross-validation supported the final model selection.

## Visualizations

The `images/` folder contains PNG files summarizing the confirmed analysis results:

- `eda_summary.png`
- `missing_values_summary.png`
- `model_metrics_comparison.png`
- `cross_validation_rmsle.png`
- `feature_importance_summary.png`
- `key_findings_summary.png`

These images use only the results recorded from the prior analysis. They do not introduce new model scores.

## Project Files

```text
assignment1/
├── data/
│   └── train.csv
├── images/
│   ├── eda_summary.png
│   ├── missing_values_summary.png
│   ├── model_metrics_comparison.png
│   ├── cross_validation_rmsle.png
│   ├── feature_importance_summary.png
│   └── key_findings_summary.png
└── links/
    └── youtube_links.md
├── notebooks/
│   └── house_prices_analysis.ipynb
├── src/
│   └── house_prices_analysis.py
├── results/
│   ├── model_metrics.csv
│   ├── cross_validation_results.csv
│   └── feature_importance_summary.csv
├── Chat_transcript.pdf
├── README.md
```

## ChatGPT Transcript

The complete ChatGPT interaction used to perform the data science analysis should be exported and added to this repository.

```text
assignment1/transcript/chat_transcript.pdf
```

## YouTube Walkthrough

```text
[Add YouTube video link here]
```

## Tools Used

- ChatGPT
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Kaggle
- GitHub
- Medium
- SaveGPT or another transcript export tool
- YouTube

## Conclusion

This project demonstrated a complete AI-assisted data science workflow using the Kaggle House Prices dataset.

The analysis showed that house quality, living space, location, age, and supporting property features play major roles in determining sale price.

Among the tested machine learning models, Gradient Boosting provided the strongest RMSLE performance and the most consistent cross-validation results.

More importantly, the project showed how an AI coding assistant can support the full data science process while still requiring human understanding, interpretation, and decision-making.
