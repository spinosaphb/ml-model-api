"""
MLModel Model
"""
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Any
from core.utils import PyObjectId

class Metrics(BaseModel):
    """
    MLModel Model Metrics
    """
    loss: float
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    epochs: Optional[int] = None


class MLModel(BaseModel):
    """
    MLModel Model
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    name: str = None
    description: str = None
    type: str = None
    metrics: Optional[Metrics] = Metrics(
        loss = .0,
        accuracy = .0,
        precision = .0,
        recall = .0,
        f1_score = .0,
        epochs = 0
    )
    created: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class MLModelResponse(BaseModel):
    """
    MLModel Model Response
    """
    id: str = Field(default_factory=str, alias='_id')
    name: str = None
    description: str = None
    type: str = None
    metrics: Optional[Metrics] = None
    created: str = None
