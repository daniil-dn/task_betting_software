from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class BetStatusBase(BaseModel):
    pass


class BetStatusInDB(BetStatusBase):
    id: int
    name_id: Optional[str]
    name: Optional[str]
    created_at: datetime


class BetStatusCreate(BetStatusBase):
    id: int
    name_id: str
    name: str


class BetStatusUpdate(BetStatusBase):
    pass
