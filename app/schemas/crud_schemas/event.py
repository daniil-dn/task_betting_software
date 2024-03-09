import decimal
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class EventBase(BaseModel):
    pass


class EventInDB(EventBase):
    id: int
    status_id: int
    coefficient: decimal.Decimal
    deadline: datetime
    updated_at: datetime
    created_at: datetime


class EventCreate(EventBase):
    coefficient: decimal.Decimal
    deadline: datetime


class EventUpdate(EventBase):
    id: int
    status_id: Optional[int] = None
    coefficient: Optional[decimal.Decimal] = None
    deadline: Optional[datetime] = None
