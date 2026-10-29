import pandas as pd
import numpy as np

HEART_COLUMNS = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach",
                 "exang","oldpeak","slope","ca","thal","target"]
HEART_NUM = ["age","trestbps","chol","thalach","oldpeak"]
HEART_CAT = ["sex","cp","fbs","restecg","exang","slope","ca","thal"]
STROKE_NUM = ["age","avg_glucose_level","bmi"]
STROKE_CAT = ["gender","hypertension","heart_disease","ever_married","work_type",
              "Residence_type","smoking_status"]
STROKE_DROP = ["id"]

def load_heart(path):
    df = pd.read_csv(path, header=None, names=HEART_COLUMNS, na_values="?")
    df["target"] = (df["target"] > 0).astype(int)
    return df

def load_stroke(path):
    df = pd.read_csv(path)
    for c in STROKE_DROP:
        if c in df.columns:
            df = df.drop(columns=c)
    df["stroke"] = df["stroke"].astype(int)
    return df
