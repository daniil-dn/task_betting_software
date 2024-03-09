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
    updated_at: datetime
    created_at: datetime


class BetCreate(BetBase):
    event_id: int
    amount: decimal.Decimal


class BetUpdate(BetBase):
    id: int
    event_id: Optional[int] = None
    amount: Optional[decimal.Decimal] = None
    status_id: Optional[int] = None
