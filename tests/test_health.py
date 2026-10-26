from fastapi.testclient import TestClient
from expense_exercise.main import app


def test_health():
    assert TestClient(app).get("/health").json() == {"status": "ok"}
