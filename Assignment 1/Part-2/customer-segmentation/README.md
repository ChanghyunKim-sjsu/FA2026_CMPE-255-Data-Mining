# Customer Segmentation with K-Means

## Overview

This experiment applies unsupervised machine learning to identify meaningful
customer segments using the Mall Customers dataset.

The clustering workflow uses:

- Age
- Annual Income
- Spending Score

K-Means clustering was evaluated using both the Elbow Method and Silhouette
Score.

---

## Dataset

The dataset contains:

- 200 customers
- 5 columns
- 0 missing values
- 0 duplicate rows

Available columns:

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

`CustomerID` was excluded because it is only an identifier.

`Gender` was not included in the initial clustering model because K-Means is
based on numerical distance.

---

## Feature Scaling

The following numerical features were standardized using `StandardScaler`:

- Age
- Annual Income
- Spending Score

Scaling was applied because K-Means relies on distance calculations and the
features use different numerical ranges.

---

## Selecting the Number of Clusters

Multiple values of `k` from 2 to 10 were evaluated.

The highest Silhouette Score was obtained at:

- **k = 6**
- **Silhouette Score = 0.428417**

The Elbow Method also showed that the reduction in inertia became more gradual
around this range.

Therefore, the final K-Means model used:

**6 clusters**

### Elbow Method

![Elbow Method](figures/elbow_method.png)

### Silhouette Score

![Silhouette Scores](figures/silhouette_scores.png)

---

## Customer Segments

The final cluster profiles were:

| Cluster | Avg Age | Avg Income | Avg Spending Score | Customers |
| ------- | ------: | ---------: | -----------------: | --------: |
| 0       |   56.33 |      54.27 |              49.07 |        45 |
| 1       |   26.79 |      57.10 |              48.13 |        39 |
| 2       |   41.94 |      88.94 |              16.97 |        33 |
| 3       |   32.69 |      86.54 |              82.13 |        39 |
| 4       |   25.00 |      25.26 |              77.61 |        23 |
| 5       |   45.52 |      26.29 |              19.38 |        21 |

The clusters can be interpreted as:

1. **Older Moderate Customers**
2. **Young Moderate Customers**
3. **High-Income Low Spenders**
4. **High-Income High Spenders**
5. **Young Low-Income High Spenders**
6. **Older Low-Income Low Spenders**

One interesting finding is that Clusters 0 and 1 have similar income and
spending behavior but differ substantially in age.

This helps explain why the three-feature model produced six clusters even
though the earlier two-dimensional income-versus-spending visualization
appeared to show approximately five groups.

---

## PCA Visualization

PCA was used to reduce the three standardized clustering features to two
dimensions for visualization.

The first two principal components explained approximately:

- PC1: 44.3%
- PC2: 33.3%
- Total: **77.6%**

![Customer Segments PCA](figures/customer_segments_pca.png)

The PCA visualization shows that the customer segments occupy generally
different regions of the reduced feature space, although some overlap remains.

PCA was used only for visualization. The K-Means model itself was trained using
all three standardized features.

---

## Results

Generated result files:

- `results/k_selection_results.csv`
- `results/cluster_profiles.csv`
- `results/customer_segments.csv`

Generated figures:

- `figures/elbow_method.png`
- `figures/silhouette_scores.png`
- `figures/customer_segments_pca.png`

---

## Conclusion

This experiment demonstrated how K-Means clustering can be used to identify
customer groups without predefined labels.

The final model used six clusters based on the Elbow Method and Silhouette
Score.

The resulting customer segments showed meaningful differences in age, income,
and spending behavior.

The experiment also demonstrated that adding Age to the clustering features can
reveal customer differences that are not visible when examining only Annual
Income and Spending Score.
