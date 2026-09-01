# Assignment 1 - House Prices Data Science Project

## Project Overview

This project explores the Kaggle **House Prices: Advanced Regression Techniques** dataset using ChatGPT as an AI-assisted data science tool.

The goal is to understand the housing dataset, perform exploratory data analysis, preprocess the data, train multiple regression models, compare their performance, and identify the most important factors affecting house prices.

The full data science workflow was completed interactively with ChatGPT, including explanations, code generation, result interpretation, and model comparison.

---

## Dataset

**Dataset:** Kaggle House Prices: Advanced Regression Techniques  
**Target Variable:** `SalePrice`

The training dataset contains:

- 1,460 rows
- 81 columns
- Numerical and categorical housing features
- Housing characteristics such as quality, size, neighborhood, garage information, basement information, and year built

The objective is to predict the final sale price of each house.

---

## Data Science Workflow

The project followed an end-to-end data science workflow:

1. Dataset understanding
2. Data quality inspection
3. Exploratory Data Analysis
4. Missing value analysis
5. Feature preprocessing
6. Train-validation split
7. Baseline model creation
8. Machine learning model training
9. Model evaluation
10. Cross-validation
11. Feature importance analysis
12. Final interpretation

---

## Exploratory Data Analysis

### Sale Price Distribution

The average house sale price was approximately:

**$180,921**

The median house sale price was approximately:

**$163,000**

The target variable was positively skewed, with a skewness of approximately:

**1.88**

This means that most houses were concentrated in the lower and middle price ranges, while a smaller number of expensive houses created a long right tail.

---

## Important Relationships

Several features showed strong relationships with house prices.

### Overall Quality

`OverallQual` had one of the strongest correlations with `SalePrice`.

**Correlation: approximately 0.791**

This suggests that the overall construction and finish quality of a house is one of the strongest predictors of its sale price.

### Above-Ground Living Area

`GrLivArea` also showed a strong positive relationship with sale price.

**Correlation: approximately 0.709**

Larger living spaces generally resulted in higher house prices.

### Neighborhood

House prices also varied significantly depending on neighborhood.

Median sale prices across neighborhoods ranged approximately from:

**$88,000 to $315,000**

This indicates that location is also an important factor in determining house value.

---

## Missing Value Analysis

Several variables contained large numbers of missing values, including:

- `PoolQC`
- `MiscFeature`
- `Alley`
- `Fence`
- `FireplaceQu`

However, some missing values represent the absence of a feature rather than bad data.

For example, a missing `PoolQC` value may simply mean that the house does not have a pool.

For this reason, missing categorical values were generally represented using a separate `"Missing"` category rather than simply deleting those rows or columns.

---

## Data Preprocessing

The following preprocessing steps were applied:

- Removed the `Id` column
- Used median imputation for missing numerical values
- Replaced missing categorical values with `"Missing"`
- Applied one-hot encoding to categorical variables
- Created approximately 301 final model features
- Split the dataset into training and validation sets
- Used an 80/20 train-validation split
- Used `random_state=42` for reproducibility

---

## Models Evaluated

Several regression approaches were compared.

| Model | RMSE | MAE | R² | RMSLE |
|---|---:|---:|---:|---:|
| Median Baseline | $88,667 | $59,568 | -0.025 | 0.432 |
| Log Linear Regression | $22,902 | $15,076 | 0.932 | 0.132 |
| Random Forest | $29,007 | $17,469 | 0.890 | ~0.148 |
| Gradient Boosting | $28,787 | $16,763 | 0.892 | **0.130** |

---

## Model Interpretation

The Log Linear Regression model achieved the best RMSE, MAE, and R² scores on the validation set.

However, the **Gradient Boosting model achieved the best RMSLE score of approximately 0.130**.

RMSLE is particularly useful for this type of housing-price problem because it measures relative prediction error and reduces the effect of very expensive houses.

Because the Kaggle House Prices competition commonly uses RMSLE-style evaluation, Gradient Boosting was selected as the final model.

---

## Cross-Validation Results

To evaluate whether the model results were stable across different subsets of the training data, 3-fold cross-validation was performed.

| Model | Mean RMSLE | Standard Deviation |
|---|---:|---:|
| Gradient Boosting | **0.138** | 0.016 |
| Random Forest | 0.148 | 0.019 |
| Log Linear Regression | 0.159 | 0.028 |

Gradient Boosting achieved the best average cross-validation RMSLE.

This provided additional evidence that the model generalized well beyond a single train-validation split.

---

## Feature Importance

The Gradient Boosting model showed that a small number of features contributed heavily to the predictions.

Two of the most important features were:

- `OverallQual` — approximately **46%**
- `GrLivArea` — approximately **17%**

Other influential factors included:

- House age
- Basement size
- Garage capacity
- Construction quality
- Neighborhood
- Additional size and quality-related features

The results suggest that house prices are strongly influenced by a combination of:

**quality + usable living space + location + property age + supporting amenities**

---

## Key Findings

The most important findings from this project were:

- Overall house quality was the strongest predictor of sale price.
- Larger above-ground living areas were generally associated with higher prices.
- Neighborhood location had a significant effect on house value.
- Missing values sometimes carried real-world meaning and should not always be treated as bad data.
- A simple baseline model performed poorly, confirming that the dataset contained useful predictive information.
- Multiple models performed well, but Gradient Boosting achieved the best RMSLE.
- Cross-validation supported the final model selection.

---

## What I Learned

This project helped me understand that data science involves more than simply training a machine learning model.

The process required:

- Understanding the problem
- Inspecting the dataset
- Making decisions about missing values
- Exploring relationships between variables
- Selecting appropriate evaluation metrics
- Comparing multiple models
- Checking model stability
- Interpreting the final results

ChatGPT helped generate code, explain techniques, and interpret results, but I still needed to evaluate whether the analysis made sense and understand why each step was necessary.

One important lesson was that the model with the best R² or RMSE is not automatically the best model for every problem. The evaluation metric must match the objective of the project.

---

## Project Artifacts

This directory contains the artifacts created during the project.

```text
assignment1/
│
├── README.md
├── chat_transcript.pdf
├── house_prices_analysis.ipynb
├── images/
├── results/
└── other project artifacts
```

Additional files may be added as the project is finalized.

---

## ChatGPT Transcript

The complete ChatGPT interaction used to perform the data science analysis is included in this repository.

**Transcript:** `chat_transcript.pdf`

The conversation was exported using SaveGPT.

---

## Medium Article

A summarized and polished version of the analysis was published as a Medium-style article.

**Medium Article:**  
[Add Medium article link here]

---

## YouTube Walkthrough

A video walkthrough explains the end-to-end project, including the dataset, analysis process, models, results, and my own interpretation of the findings.

**YouTube Video:**  
[Add YouTube video link here]

---

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
- SaveGPT

---

## Conclusion

This project demonstrated a complete AI-assisted data science workflow using the Kaggle House Prices dataset.

The analysis showed that house quality, living space, location, age, and supporting property features play major roles in determining sale price.

Among the tested machine learning models, Gradient Boosting provided the strongest RMSLE performance and the most consistent cross-validation results.

More importantly, the project demonstrated how an AI coding assistant can support the full data science process while still requiring human understanding, interpretation, and decision-making.
