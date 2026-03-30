from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ExperimentCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ExperimentResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}