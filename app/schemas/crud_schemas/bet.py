import decimal
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class BetBase(BaseModel):
    pass


class BetInDB(BetBase):
    id: int
    event_id: int
    status_id: int
    amount: decimal.Decimal
    updated_at: Optional[datetime] = None
    created_at: datetime


class BetCreate(BetBase):
    event_id: int
    amount: decimal.Decimal
    status_id: int


class BetUpdate(BetBase):
    id: int
    event_id: Optional[int] = None
    amount: Optional[decimal.Decimal] = None
    status_id: Optional[int] = None
