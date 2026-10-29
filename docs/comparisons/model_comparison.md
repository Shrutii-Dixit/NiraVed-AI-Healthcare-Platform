# Model Comparison (held-out test set)

See CSVs in this folder: heart_comparison.csv, stroke_comparison.csv.

## Heart (best: LogisticRegression, test AUC 0.966)
- LogisticRegression: AUC 0.966, F1 0.867
- RandomForest: AUC 0.948, F1 0.900
- LightGBM: AUC 0.949, F1 0.871
- XGBoost: AUC 0.932, F1 0.867

## Stroke (best: LogisticRegression, test AUC 0.844)
- LogisticRegression: AUC 0.844, F1 0.236, recall 0.80
- RandomForest: AUC 0.801, F1 0.130
- LightGBM: AUC 0.783, F1 0.186
- XGBoost: AUC 0.780, F1 0.194

Note: stroke is highly imbalanced (~5% positive); AUC is the primary metric, threshold can be lowered to boost recall.
Plots: heart_roc.png, stroke_roc.png, *_calibration.png, *_shap.png, *_cm.png
