import os, json, joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import calibration_curve
from sklearn.metrics import (roc_auc_score, average_precision_score, accuracy_score,
                             precision_score, recall_score, f1_score, confusion_matrix,
                             roc_curve, precision_recall_curve, brier_score_loss)
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
import shap

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "raw")
MODELS = os.path.join(BASE, "models")
OUT = os.path.join(BASE, "docs", "comparisons")
os.makedirs(os.path.join(MODELS, "heart"), exist_ok=True)
os.makedirs(os.path.join(MODELS, "stroke"), exist_ok=True)
os.makedirs(OUT, exist_ok=True)

from src.niraved.common.preprocessing import (load_heart, load_stroke, HEART_NUM, HEART_CAT,
                                              STROKE_NUM, STROKE_CAT)

RANDOM = 42

def make_preprocessor(num_cols, cat_cols):
    return ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                          ("sc", StandardScaler())]), num_cols),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                          ("oh", OneHotEncoder(handle_unknown="ignore"))]), cat_cols),
    ])

def make_pipeline(model, num_cols, cat_cols, balance=False):
    pre = make_preprocessor(num_cols, cat_cols)
    steps = [("pre", pre)]
    if balance:
        steps.append(("smote", SMOTE(random_state=RANDOM)))
    steps.append(("clf", model))
    return ImbPipeline(steps)

def train_module(name, df, target, num_cols, cat_cols, balance_models):
    X = df[num_cols + cat_cols]
    y = df[target].values
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=RANDOM)
    pos = (ytr == 1).sum(); neg = (ytr == 0).sum()
    models = {
        "LogisticRegression": LogisticRegression(max_iter=2000, class_weight="balanced"),
        "RandomForest": RandomForestClassifier(n_estimators=400, class_weight="balanced", random_state=RANDOM, n_jobs=-1),
        "XGBoost": XGBClassifier(n_estimators=500, learning_rate=0.05, max_depth=4,
                                 scale_pos_weight=neg/pos, random_state=RANDOM, eval_metric="auc", n_jobs=-1),
        "LightGBM": LGBMClassifier(n_estimators=500, learning_rate=0.05, class_weight="balanced", random_state=RANDOM, n_jobs=-1),
    }
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM)
    rows = []
    fitted = {}
    for mname, m in models.items():
        pipe = make_pipeline(m, num_cols, cat_cols, balance=(mname in balance_models))
        res = cross_validate(pipe, Xtr, ytr, cv=cv, scoring=["roc_auc","average_precision","accuracy"], n_jobs=-1)
        pipe.fit(Xtr, ytr)
        fitted[mname] = pipe
        proba = pipe.predict_proba(Xte)[:, 1]
        pred = (proba >= 0.5).astype(int)
        rows.append({
            "model": mname,
            "cv_auc": res["test_roc_auc"].mean(),
            "cv_auc_std": res["test_roc_auc"].std(),
            "cv_pr": res["test_average_precision"].mean(),
            "cv_acc": res["test_accuracy"].mean(),
            "test_auc": roc_auc_score(yte, proba),
            "test_pr": average_precision_score(yte, proba),
            "test_acc": accuracy_score(yte, pred),
            "test_precision": precision_score(yte, pred, zero_division=0),
            "test_recall": recall_score(yte, pred, zero_division=0),
            "test_f1": f1_score(yte, pred, zero_division=0),
            "brier": brier_score_loss(yte, proba),
        })
        print(f"[{name}] {mname}: cvAUC={rows[-1]['cv_auc']:.3f} testAUC={rows[-1]['test_auc']:.3f} F1={rows[-1]['test_f1']:.3f}")

    resdf = pd.DataFrame(rows).sort_values("test_auc", ascending=False)
    resdf.to_csv(os.path.join(OUT, f"{name}_comparison.csv"), index=False)

    # best model by test AUC
    best_name = resdf.iloc[0]["model"]
    best_pipe = fitted[best_name]
    joblib.dump(best_pipe, os.path.join(MODELS, name, "best_model.joblib"))
    joblib.dump({"num_cols": num_cols, "cat_cols": cat_cols, "target": target}, os.path.join(MODELS, name, "meta.joblib"))

    # SHAP on RandomForest (explainability)
    try:
        shap_pipe = fitted.get("RandomForest", best_pipe)
        Xte_t = shap_pipe.named_steps["pre"].transform(Xte)
        clf = shap_pipe.named_steps["clf"]
        explainer = shap.TreeExplainer(clf)
        sv = explainer.shap_values(Xte_t)
        sv = np.array(sv)
        if sv.ndim == 3:
            sv = sv[:, :, 1]
        elif isinstance(sv, list):
            sv = sv[1]
        names = list(shap_pipe.named_steps["pre"].get_feature_names_out())
        imp = np.abs(sv).mean(axis=0)
        order = np.argsort(imp)[::-1][:15]
        fig, ax = plt.subplots(figsize=(8,6))
        ax.barh([names[i] for i in order][::-1], [imp[i] for i in order][::-1])
        ax.set_title(f"{name} SHAP importance (RF)")
        plt.tight_layout()
        plt.savefig(os.path.join(OUT, f"{name}_shap.png"), dpi=120, bbox_inches="tight")
        plt.close()
    except Exception as e:
        print("SHAP skipped:", e)

    # ROC plot
    fig, ax = plt.subplots(figsize=(7,6))
    for mname, pipe in fitted.items():
        proba = pipe.predict_proba(Xte)[:,1]
        fpr, tpr, _ = roc_curve(yte, proba)
        ax.plot(fpr, tpr, label=f"{mname} (AUC={roc_auc_score(yte,proba):.3f})")
    ax.plot([0,1],[0,1],"k--",alpha=0.4)
    ax.set_xlabel("FPR"); ax.set_ylabel("TPR"); ax.set_title(f"{name} ROC")
    ax.legend(); plt.tight_layout()
    plt.savefig(os.path.join(OUT, f"{name}_roc.png"), dpi=120); plt.close()

    # calibration plot
    fig, ax = plt.subplots(figsize=(7,6))
    for mname, pipe in fitted.items():
        proba = pipe.predict_proba(Xte)[:,1]
        pt, pp = calibration_curve(yte, proba, n_bins=10)
        ax.plot(pp, pt, marker="o", label=mname)
    ax.plot([0,1],[0,1],"k--",alpha=0.4)
    ax.set_xlabel("Predicted"); ax.set_ylabel("Observed"); ax.set_title(f"{name} Calibration")
    ax.legend(); plt.tight_layout()
    plt.savefig(os.path.join(OUT, f"{name}_calibration.png"), dpi=120); plt.close()

    # confusion matrix for best
    proba = best_pipe.predict_proba(Xte)[:,1]
    pred = (proba >= 0.5).astype(int)
    cm = confusion_matrix(yte, pred)
    fig, ax = plt.subplots(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_title(f"{name} Best ({best_name}) CM"); ax.set_xlabel("Pred"); ax.set_ylabel("True")
    plt.tight_layout(); plt.savefig(os.path.join(OUT, f"{name}_cm.png"), dpi=120); plt.close()

    print(f"[{name}] BEST: {best_name}")
    return resdf, best_name

if __name__ == "__main__":
    # Heart
    hdf = load_heart(os.path.join(DATA, "heart_cleveland.csv"))
    hres, hbest = train_module("heart", hdf, "target", HEART_NUM, HEART_CAT, {"XGBoost","LightGBM"})
    # Stroke
    sdf = load_stroke(os.path.join(DATA, "stroke_data.csv"))
    sres, sbest = train_module("stroke", sdf, "stroke", STROKE_NUM, STROKE_CAT, {"XGBoost","LightGBM"})
    print("\n=== DONE ===")
    print("Heart best:", hbest); print(hres.to_string(index=False))
    print("Stroke best:", sbest); print(sres.to_string(index=False))
