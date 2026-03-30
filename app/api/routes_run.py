from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.run import RunCreate, RunResponse
from app.services.run import create_run, list_runs, compare_runs
from typing import Any

router = APIRouter()

@router.post("", response_model=RunResponse, status_code=201)
def create(data: RunCreate, db: Session = Depends(get_db)):
    return create_run(db, data)

@router.get("/compare")
def compare(
    experiment_id: str = Query(...),
    metric: str = Query(...),
    top_k: int = Query(5),
    db: Session = Depends(get_db)
) -> dict[str, Any]:
    return compare_runs(db, experiment_id, metric, top_k)

@router.get("/{experiment_id}", response_model=list[RunResponse])
def list_all(experiment_id: str, db: Session = Depends(get_db)):
    return list_runs(db, experiment_id)