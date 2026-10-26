# Expense Exercise, Python candidate starter

You will receive a small Python backend for review during the technical interview.
This starter contains only a health endpoint and database configuration.

## Setup

Python 3.11+:

```bash
python -m venv .venv
# Activate .venv (Windows: .venv\\Scripts\\activate, Linux: source .venv/bin/activate)
pip install -e '.[dev]'
uvicorn expense_exercise.main:app --reload
pytest -q
```

Open http://127.0.0.1:8000/health and http://127.0.0.1:8000/docs.
An additional feature branch/patch is provided at interview time.
