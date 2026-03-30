from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any
from app.models.run import RunStatus

class RunCreate(BaseModel):
    experiment_id: str
    status: RunStatus = RunStatus.running
    metrics: Optional[dict[str, Any]] = None
    config: Optional[dict[str, Any]] = None
    tags: Optional[dict[str, Any]] = None

class RunResponse(BaseModel):
    id: str
    experiment_id: str
    status: RunStatus
    metrics: Optional[dict[str, Any]] = None
    config: Optional[dict[str, Any]] = None
    tags: Optional[dict[str, Any]] = None
    created_at: datetime

    model_config = {"from_attributes": True}