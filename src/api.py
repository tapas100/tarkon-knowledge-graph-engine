from fastapi import FastAPI

app = FastAPI(title="Tarkon Knowledge Graph Engine", version="0.1.0")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "service": "tarkon-knowledge-graph-engine"}


@app.get("/concepts")
async def list_concepts() -> list:
    raise NotImplementedError("Knowledge graph engine not yet implemented")


@app.get("/students/{student_id}/mastery")
async def get_mastery(student_id: str) -> dict:
    raise NotImplementedError("Knowledge graph engine not yet implemented")
