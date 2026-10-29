import os, joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI(title="NiraVed API")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

heart_pipe = joblib.load(os.path.join(BASE, "models", "heart", "best_model.joblib"))
stroke_pipe = joblib.load(os.path.join(BASE, "models", "stroke", "best_model.joblib"))
cad_pipe = joblib.load(os.path.join(BASE, "models", "cad", "best_model.joblib"))
heart_meta = joblib.load(os.path.join(BASE, "models", "heart", "meta.joblib"))
stroke_meta = joblib.load(os.path.join(BASE, "models", "stroke", "meta.joblib"))
cad_meta = joblib.load(os.path.join(BASE, "models", "cad", "meta.joblib"))

class HeartInput(BaseModel):
    age: float; sex: float; cp: float; trestbps: float; chol: float
    fbs: float; restecg: float; thalach: float; exang: float
    oldpeak: float; slope: float; ca: float; thal: float

class StrokeInput(BaseModel):
    gender: str; age: float; hypertension: int; heart_disease: int
    ever_married: str; work_type: str; Residence_type: str
    avg_glucose_level: float; bmi: float; smoking_status: str

@app.get("/")
def root():
    return {"status": "ok", "modules": ["heart", "stroke", "cad"]}

@app.get("/meta/cad")
def meta_cad():
    return {"features": cad_meta["feature_columns"]}

@app.post("/predict/heart")
def predict_heart(x: HeartInput):
    df = pd.DataFrame([x.dict()])
    proba = float(heart_pipe.predict_proba(df)[0, 1])
    return {"module": "heart", "risk_probability": proba,
            "risk_label": "high" if proba >= 0.5 else "low"}

@app.post("/predict/stroke")
def predict_stroke(x: StrokeInput):
    df = pd.DataFrame([x.dict()])
    proba = float(stroke_pipe.predict_proba(df)[0, 1])
    return {"module": "stroke", "risk_probability": proba,
            "risk_label": "high" if proba >= 0.5 else "low"}

@app.post("/predict/cad")
def predict_cad(payload: dict):
    cols = cad_meta["feature_columns"]
    row = {c: payload.get(c, None) for c in cols}
    df = pd.DataFrame([row], columns=cols)
    proba = float(cad_pipe.predict_proba(df)[0, 1])
    return {"module": "cad", "risk_probability": proba,
            "risk_label": "high" if proba >= 0.5 else "low"}
