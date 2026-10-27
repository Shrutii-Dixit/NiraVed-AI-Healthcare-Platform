# Contributing to NiraVed

NiraVed is currently a planning-stage research prototype. Contributions should preserve the two-module scope and distinguish proposed work from implemented and measured results.

## Set up

Clone the repository, create a virtual environment, and install the proposed dependencies:

```bash
git clone https://github.com/Shrutii-Dixit/NiraVed-AI-Healthcare-Platform.git
cd NiraVed-AI-Healthcare-Platform
python -m venv .venv
python -m pip install -r requirements.txt
```

The stack is provisional and has not been verified. No executable app or tests are currently available; see [tests/README.md](tests/README.md).

## Branch and commit workflow

1. Check the issue and coordinate ownership before starting overlapping work.
2. Branch from an up-to-date `main` using `feature/<issue>-short-name`, `docs/<issue>-short-name`, or `fix/<issue>-short-name`.
3. Make focused changes and update relevant documentation.
4. Use conventional commit prefixes such as `docs:`, `feat:`, `fix:`, `test:`, or `chore:` with a concise imperative description.
5. Open a pull request with the repository template. Link its issue and request review from a teammate.
6. Address review comments and merge only after agreed acceptance criteria are met.

Initial repository setup may be committed directly to `main` by the maintainer; normal collaborative work should use pull requests.

## Quality and research integrity

- Run available checks and state exactly what was run. Do not claim a test passed if it was not run.
- Keep heart and stroke datasets, transformations, evaluation, and model artifacts separate.
- Record dataset source, provenance, licence/terms, label definition, and known limitations before use. Obtain data from authorized sources only.
- Never commit patient records, restricted or large datasets, model binaries, caches, secrets, or generated outputs.
- Never include real credentials in commits. Local `.env` files are ignored; no environment variables are currently required.
- Cite original sources and verify authors, title, year, venue, and DOI/URL. Clearly separate source findings from team interpretation.
- Report actual experimental methods and results only. Never invent metrics, citations, screenshots, or implementation status.
- Keep user-facing claims educational and non-diagnostic; document privacy and safety implications.

## Review expectations

Reviewers should check correctness, reproducibility, leakage safeguards, source citations, privacy, responsible wording, and consistency between code and documentation. Every member shares responsibility for literature review, requirements, documentation, testing, and presentation.
