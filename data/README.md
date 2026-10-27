# Data policy and dataset register

No dataset is selected or included yet. Obtain candidate datasets from their original authorized sources and verify access terms before use. Record the source link, provenance, licence/terms, collection method, population, schema, target definition, preprocessing, and known limitations for each module before experiments begin.

| Module | Dataset/source | Licence and access terms | Target and population | Status |
|---|---|---|---|---|
| Heart | Not selected | Not verified | To be documented | Planned |
| Stroke risk | Not selected | Not verified | To be documented | Planned |

Keep raw files immutable and out of Git. Do not commit personal or patient data, restricted material, or large datasets. Store permitted local copies under `raw/` and reproducible transformed outputs under `processed/`; both directories are ignored except for `.gitkeep` placeholders. Keep data dictionaries and acquisition instructions here without reproducing restricted data.
