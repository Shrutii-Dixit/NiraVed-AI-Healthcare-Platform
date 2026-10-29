# Run NiraVed locally

## Train models
```powershell
cd C:\Users\shrut\Documents\NiraVed-AI-Healthcare-Platform
$env:PYTHONPATH="."
python ml\train_all.py
python ml\train_cad.py
```
Outputs: models/, docs/comparisons/ (metrics + plots).

## Backend (FastAPI)
```powershell
$env:PYTHONPATH="."
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```
API docs: http://127.0.0.1:8000/docs  (heart, stroke, cad, meta/cad)

## Frontend
Open frontend/index.html in a browser (backend must be running). CAD detailed form: frontend/cad.html
```
- `docs/research/research_papers.md` — top papers
- `docs/comparisons/model_comparison.md` — results + plots
- `docs/comparisons/cad_comparison.csv` — CAD model results
