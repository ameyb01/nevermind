from sqlalchemy.orm import Session
from app.models.experiment import Experiment
from app.schemas.experiment import ExperimentCreate
from fastapi import HTTPException

def create_experiment(db: Session, data: ExperimentCreate) -> Experiment:
    existing = db.query(Experiment).filter(Experiment.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Experiment name already exists")
    
    experiment = Experiment(
        name=data.name,
        description=data.description
    )
    db.add(experiment)
    db.commit()
    db.refresh(experiment)
    return experiment

def list_experiments(db: Session) -> list[Experiment]:
    return db.query(Experiment).order_by(Experiment.created_at.desc()).all()

def get_experiment(db: Session, experiment_id: str) -> Experiment:
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not experiment:
        raise HTTPException(status_code=404, detail="Experiment not found")
    return experiment