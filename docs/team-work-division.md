# Provisional Team Work Division

This is a proposed allocation for exactly four team members. Confirm names, assignments, and scope with the team and faculty before treating it as final. Every member contributes to literature review, requirements, documentation, testing, and final presentation; integration is a shared responsibility.

## Roles and deliverables

| Member | Primary role | Responsibilities and individual deliverables |
|---|---|---|
| Member 1 | Heart disease ML | Review heart literature; investigate dataset provenance and terms; conduct EDA and preprocessing; compare baseline and candidate models; evaluate and document actual results. |
| Member 2 | Brain / stroke-risk ML | Review stroke literature; verify dataset; conduct EDA and preprocessing; address class imbalance; develop, evaluate, and document models. |
| Member 3 | Explainable AI and research | Review XAI literature; assess SHAP and alternatives; coordinate explanation work with Members 1 and 2; maintain literature review and research-gap analysis; assess reliability and limitations. |
| Member 4 | Application, integration, and repository | Coordinate proposed UI/API architecture; integrate modules after they are ready; maintain repository structure and Git workflow; coordinate integration testing and application validation. |

## Dependencies and shared responsibilities

Dataset and label verification precedes modeling. Members 1 and 2 share schemas and evaluation conventions with Member 3 so explanation methods remain model-appropriate. Member 4 can define integration contracts only after module feature schemas and artifacts are documented. All members review each other's methods, documentation, tests, sources, and presentation material. No member is solely responsible for all documentation or integration.

## Shared milestones

| Milestone | Participants | Evidence | Status |
|---|---|---|---|
| Agree scope, requirements, and final role allocation | All; faculty review | Approved requirements and named roster | Pending |
| Verify candidate datasets and literature | All; module leads coordinate | Source/terms records and verified citations | Planned |
| Complete independent module baselines and evaluations | Members 1 and 2; peer review by 3 | Reproducible reports with real metrics | Planned |
| Review explanation behavior and limitations | Member 3 with 1 and 2 | Method rationale and reviewed examples | Planned |
| Integrate and validate application | Member 4 with all module owners | PRs, integration checks, safety review | Planned |
| Final report and presentation | All | Reviewed deliverables and evidence | Planned |

## Weekly progress tracker

Duplicate a row per week. Owners are placeholders until the team assigns work; no dates or completed tasks are implied.

| Week | Owner | Deliverable | Status | Evidence / issue or PR |
|---|---|---|---|---|
| To schedule | Member 1 | Heart research/data progress | Not started | — |
| To schedule | Member 2 | Stroke research/data progress | Not started | — |
| To schedule | Member 3 | Literature/XAI progress | Not started | — |
| To schedule | Member 4 | Architecture/repository progress | Not started | — |

Each owner records actual work and evidence. Never invent accuracy, citations, or completion claims.

## Names and approval

| Placeholder | Team member name | Faculty approval |
|---|---|---|
| Member 1 | To be agreed | Pending |
| Member 2 | To be agreed | Pending |
| Member 3 | To be agreed | Pending |
| Member 4 | To be agreed | Pending |

## Meeting and GitHub review

Agree a regular team check-in cadence with the faculty guide. Track each deliverable as an issue with owner, acceptance criteria, dependencies, priority, and status. Use focused branches and pull requests; request peer review, link related issues, document evidence, and resolve comments before merge. Review actual results, source integrity, privacy, and safety wording together. The initial allocation is provisional and should be revisited as workload changes.
