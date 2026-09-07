# California Housing – Linear Model Pipeline

This project is about predicting median house values using the California Housing dataset.

I explored the data, split it into training and test sets, and compared different linear models:
- Linear Regression
- Ridge
- Lasso
- RidgeCV

I used StandardScaler with the regularized models and 5-fold cross-validation for model comparison and tuning.

## Results

| Model | CV R² |
|---|---:|
| Baseline | -0.002 |
| Linear Regression | 0.840 |
| Ridge | 0.840 |
| Lasso | -0.002 |
| RidgeCV Pipeline | 0.840 |

The final RidgeCV model selected **alpha = 1.0**.

The final model achieved a **Test R² of 0.838**, which is very close to the CV score of 0.840.

## Final Model

I selected RidgeCV because it gave good performance while keeping all features in the model. Lasso performed poorly with the default settings and reduced all feature coefficients to zero.

The coefficient chart was used to understand which features had more influence on the predicted house value.

## Files

- `notebook.ipynb` – complete analysis
- `coefficients.png` – coefficient interpretation chart
- `comparison_table.csv` – model comparison results
- `README.md` – project summary

## How to Run

Open `Linear_model_pipeline.ipynb` in Jupyter Notebook and run the cells from top to bottom.