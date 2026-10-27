# Proposed User Stories

All stories are proposed and remain unimplemented. Priorities: Must, Should, Could.

| ID | User story | Priority | Acceptance criteria | Status |
|---|---|---|---|---|
| US-01 | As a user, I want to select the heart module, so that I enter features for the correct research target. | Must | Heart module identity and dataset-defined target are clearly identified. | Proposed |
| US-02 | As a user, I want to enter and validate structured heart features, so that incomplete or invalid values are caught before inference. | Must | Required fields, types, category choices, and reviewed ranges are validated with understandable messages. | Proposed |
| US-03 | As a user, I want to view the heart model output, so that I can understand its dataset-defined estimate. | Must | Output is labeled as an estimate, includes model limitations, and makes no diagnosis claim. | Proposed |
| US-04 | As a user, I want to select the stroke-risk module, so that I use the separate stroke classification workflow. | Must | Stroke-risk scope is distinguished from tumour, MRI, and general brain disease detection. | Proposed |
| US-05 | As a user, I want to view the stroke model output, so that I can understand its dataset-defined estimate. | Must | Output identifies uncertainty and does not imply that low score rules out a stroke. | Proposed |
| US-06 | As a user, I want to understand contributing features, so that I can see how the model formed its output. | Should | Explanation names the method and says attribution is not causation. | Proposed |
| US-07 | As a user, I want to see model limitations and safety notices, so that I do not mistake research output for medical advice. | Must | Persistent notice states non-diagnostic use and advises professional care as appropriate. | Proposed |
| US-08 | As a user, I want missing or invalid input handled clearly, so that I can correct it without exposing private data. | Must | Invalid requests are rejected safely and messages do not expose internal details. | Proposed |
| US-09 | As a researcher, I want reproducible training and evaluation workflows, so that I can compare models without leakage. | Must | Data splits, transformations, seeds, baselines, and metrics are recorded; test set is held out. | Proposed |
| US-10 | As a researcher, I want to document results with verified sources, so that claims are traceable and reproducible. | Must | Each result links to an experiment and verified source; no fabricated metrics/citations. | Proposed |
| US-11 | As a team member, I want to record actual work and evidence, so that project progress and contributions are reviewable. | Should | Issue/PR and tracker identify owner, deliverable, status, and evidence. | Proposed |
| US-12 | As a team member, I want to reproduce another member's experiment, so that results can be reviewed consistently. | Should | Data version, source, environment, protocol, and commands are documented sufficiently. | Proposed |
