import decimal
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EventInDB(BaseModel):
    id: int
    status_id: Optional[int]
    coefficient: decimal.Decimal
    deadline_dt: datetime
    updated_at: Optional[datetime]
    created_at: datetime


class EventCreate(BaseModel):
    coefficient: decimal.Decimal
    deadline_dt: datetime
    status_id: int


class EventUpdate(BaseModel):
    id: int
    status_id: Optional[int] = None
    coefficient: Optional[decimal.Decimal] = None
    deadline_dt: Optional[datetime] = None
