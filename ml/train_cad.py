import os, json, joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, f1_score, accuracy_score
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "raw", "heart_subtypes", "cad", "Z-Alizadeh sani dataset.xlsx")
MODELS = os.path.join(BASE, "models", "cad")
os.makedirs(MODELS, exist_ok=True)
OUT = os.path.join(BASE, "docs", "comparisons")
os.makedirs(OUT, exist_ok=True)

df = pd.read_excel(DATA)
df["target"] = (df["Cath"] == "Cad").astype(int)
y = df["target"].values
X = df.drop(columns=["Cath", "target"])
num_cols = [c for c in X.columns if pd.api.types.is_numeric_dtype(X[c])]
cat_cols = [c for c in X.columns if c not in num_cols]
# drop constant columns
for c in list(X.columns):
    if X[c].nunique(dropna=True) <= 1:
        X = X.drop(columns=c)
        if c in num_cols: num_cols.remove(c)
        if c in cat_cols: cat_cols.remove(c)

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
pos = (ytr==1).sum(); neg=(ytr==0).sum()

def pre():
    return ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("sc", StandardScaler())]), num_cols),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                          ("oh", OneHotEncoder(handle_unknown="ignore"))]), cat_cols),
    ])

models = {
    "LogisticRegression": LogisticRegression(max_iter=2000, class_weight="balanced"),
    "RandomForest": RandomForestClassifier(n_estimators=400, class_weight="balanced", random_state=42, n_jobs=-1),
    "XGBoost": XGBClassifier(n_estimators=500, learning_rate=0.05, max_depth=4, scale_pos_weight=neg/pos, random_state=42, eval_metric="auc", n_jobs=-1),
    "LightGBM": LGBMClassifier(n_estimators=500, learning_rate=0.05, class_weight="balanced", random_state=42, n_jobs=-1),
}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
rows=[]; fitted={}
for name,m in models.items():
    pipe = ImbPipeline([("pre", pre()), ("smote", SMOTE(random_state=42)), ("clf", m)])
    res = cross_validate(pipe, Xtr, ytr, cv=cv, scoring=["roc_auc","accuracy"], n_jobs=-1)
    pipe.fit(Xtr, ytr)
    fitted[name]=pipe
    proba=pipe.predict_proba(Xte)[:,1]
    pred=(proba>=0.5).astype(int)
    rows.append({"model":name,"cv_auc":res["test_roc_auc"].mean(),"test_auc":roc_auc_score(yte,proba),
                 "test_acc":accuracy_score(yte,pred),"test_f1":f1_score(yte,pred,zero_division=0)})
    print(f"[CAD] {name}: cvAUC={rows[-1]['cv_auc']:.3f} testAUC={rows[-1]['test_auc']:.3f} F1={rows[-1]['test_f1']:.3f}")

rdf = pd.DataFrame(rows).sort_values("test_auc", ascending=False)
rdf.to_csv(os.path.join(OUT, "cad_comparison.csv"), index=False)
best = rdf.iloc[0]["model"]
joblib.dump(fitted[best], os.path.join(MODELS, "best_model.joblib"))
joblib.dump({"num_cols":num_cols,"cat_cols":cat_cols,"feature_columns":list(X.columns)}, os.path.join(MODELS, "meta.joblib"))
print("[CAD] BEST:", best)
print(rdf.to_string(index=False))
