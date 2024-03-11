from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EventStatusInDB(BaseModel):
    id: int
    name_id: Optional[str]
    name: Optional[str]
    created_at: datetime


class EventStatusCreate(BaseModel):
    id: int
    name_id: str
    name: str


class EventStatusUpdate(BaseModel):
    pass
