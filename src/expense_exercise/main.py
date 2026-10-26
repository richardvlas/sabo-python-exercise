from fastapi import FastAPI

app = FastAPI(title="Python Expense Exercise")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
