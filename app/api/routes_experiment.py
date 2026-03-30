from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.experiment import ExperimentCreate, ExperimentResponse
from app.services.experiment import create_experiment, list_experiments

router = APIRouter()

@router.post("", response_model=ExperimentResponse, status_code=201)
def create(data: ExperimentCreate, db: Session = Depends(get_db)):
    return create_experiment(db, data)

@router.get("", response_model=list[ExperimentResponse])
def list_all(db: Session = Depends(get_db)):
    return list_experiments(db)