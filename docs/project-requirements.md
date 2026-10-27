# Project Requirements

## Overview and motivation

NiraVed is a B.Tech CSE research prototype intended to study whether explainable tabular ML workflows can communicate dataset-defined heart disease and stroke-risk classifications responsibly. Cost anxiety and uncertainty motivate the broader idea, but healthcare navigation is not part of the initial implementation.

## Problem and objectives

The initial problem is to develop and independently evaluate two bounded classifiers from structured features, document data and model limitations, and assess suitable explanations. Objectives are to review domain methods; verify data provenance and label meaning; prevent leakage; compare baselines and candidate models; report meaningful metrics; and communicate uncertainty without suggesting diagnosis.

## Scope, exclusions, decisions, and assumptions

| Item | Classification | Detail |
|---|---|---|
| Heart disease and structured stroke-risk classification | Confirmed project scope | Separate targets and evaluation; heart target follows its dataset definition |
| React UI and FastAPI backend | Existing design decision, provisional | Retained from the current project README; implementation and contracts are not finalized |
| Python tabular ML stack | Proposed decision | pandas, NumPy, scikit-learn; SHAP where suitable |
| Dataset choice, feature lists, split details | Requires research/faculty review | No source or target data has been verified |
| User-facing risk categories | Assumption | Must be based on validation-set threshold selection and reviewed wording |
| Database and accounts | Out of scope for MVP | Stateless inference and no input storage by default |
| Medical diagnosis, treatment advice, MRI/tumour detection, universal brain classification | Excluded | Not supported by initial scope or evidence |

## Requirements register

Priority: **Must** = essential to the research prototype; **Should** = expected if feasible; **Could** = useful extension. Status is **Planned** unless stated otherwise. Acceptance criteria describe evidence required before marking complete.

### Functional requirements

| ID | Requirement | Priority | Acceptance criteria | Status |
|---|---|---|---|---|
| FR-01 | Maintain distinct heart and stroke-risk modules and dataset-defined targets. | Must | Each has its own documented target, data dictionary, pipeline, and evaluation report. | Planned |
| FR-02 | Verify and document every dataset before use. | Must | Source, provenance, licence/terms, collection context, label, and limitations are recorded and reviewed. | Planned |
| FR-03 | Build leakage-safe preprocessing for each module. | Must | All fitted transforms operate within training folds; test data is not used for fitting or tuning. | Planned |
| FR-04 | Compare simple baselines with suitable candidate models. | Must | Reproducible protocol and model comparison are recorded for each module. | Planned |
| FR-05 | Evaluate heart and stroke independently. | Must | Module-specific held-out results and confusion matrices are documented; stroke metrics address imbalance. | Planned |
| FR-06 | Explain model behavior where suitable. | Should | Method choice, scope, stability limits, and representative explanation behavior are documented. | Planned |
| FR-07 | Validate user inputs in a future application. | Must | Required fields, types, ranges, and invalid/missing cases are checked before inference. | Planned |
| FR-08 | Display non-diagnostic output and limitations in a future UI. | Must | Screens and wording identify an estimate, explain key limitations, and do not claim diagnosis. | Planned |
| FR-09 | Keep inference separate from training. | Must | Future inference loads versioned evaluated artifacts and does not fit models on user requests. | Planned |
| FR-10 | Present provenance and evidence in research documentation. | Must | Citations are verified and source findings are distinct from team interpretation. | Planned |

### Non-functional requirements

| ID | Requirement | Priority | Acceptance criteria | Status |
|---|---|---|---|---|
| NFR-01 | Reproducibility | Must | Code, dependency proposal/lock strategy, seeds, data versions, and experiment protocol are recorded sufficiently to reproduce permitted experiments. | Planned |
| NFR-02 | Privacy by design | Must | No health-input storage by default; no identifiable health data in logs or repository. | Planned |
| NFR-03 | Security | Must | Secrets are not committed; input validation and transport protections are addressed before deployment. | Planned |
| NFR-04 | Modularity | Should | Heart and stroke pipelines can be trained and evaluated independently with shared utilities isolated. | Planned |
| NFR-05 | Responsible communication | Must | Outputs are framed as educational estimates, never diagnoses or guaranteed outcomes. | Planned |
| NFR-06 | Maintainable documentation | Should | Requirements, architecture, workflow, and experiment decisions stay aligned with implementation. | Planned |

## Data and research safeguards

Datasets must have traceable provenance and acceptable use terms. Dataset-dependent requirements include review of label meaning, missingness, duplicates, outliers, population, subgroup representation, and potential proxy or target leakage. Keep raw data immutable. Use split-aware pipelines for imputation, encoding, scaling, feature selection, and resampling. Any resampling must happen only inside training folds. Document transformations and never combine module datasets without a research justification.

## Evaluation and explainability requirements

Use a suitable split design with a final untouched test set. Report precision, recall/sensitivity, specificity, F1-score, confusion matrix, and ROC-AUC when meaningful. For imbalanced stroke classification, include precision-recall analysis, class counts, and uncertainty; accuracy alone is insufficient. Consider calibration and Brier score before describing outputs as probabilities. Thresholds are selected only with validation data. Explainability (SHAP or an alternative) must be model-appropriate and described as model attribution, not causal evidence.

## UI, integration, and safety

The proposed React UI and FastAPI API must validate inputs, route to the correct independent module, handle unavailable models and malformed values safely, and clearly show limitations. Do not store input data by default. Any deployment, account, persistence, or external integration requires a separately reviewed privacy and security design.

## Testing and acceptance

The project setup is accepted when documentation agrees on scope/status; each selected dataset has reviewed provenance and terms; each module has a reproducible leakage-safe pipeline and baseline comparison; held-out evaluation is reported honestly; explanations and safety language are reviewed; and available tests pass with commands documented. No implementation acceptance is claimed yet. See [tests/README.md](../tests/README.md).

## Constraints and assumptions

This is a student research project with limited time and data. The selected public datasets may be small, imbalanced, old, or population-specific. React and FastAPI are retained from the existing design but are not finalized through an implementation decision. Dependency constraints are proposals, not verified compatibility claims. Faculty approval is pending for final datasets, methodology, and team role allocation.

## Out of scope and future enhancements

Initial exclusions: diagnosis, treatment recommendations, clinical deployment, MRI analysis, universal disease detection, OCR, cost estimation, hospital ranking, insurance advice, and live emergency/doctor integrations. Potential future work requires independent requirements, data, safety review, and evaluation.
