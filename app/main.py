from fastapi import FastAPI
from app.core.config import settings
from app.db.database import Base, engine
from app.api.routes_experiment import router as experiment_router
from app.api.routes_run import router as run_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="Experiment tracking service. Because someone has to remember.",
    version="0.1.0"
)

app.include_router(experiment_router, prefix="/experiments", tags=["experiments"])
app.include_router(run_router, prefix="/runs", tags=["runs"])

@app.get("/health")
def health():
    return {"status": "ok", "service": settings.APP_NAME}