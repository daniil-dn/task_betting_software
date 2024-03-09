from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class EventStatusBase(BaseModel):
    pass


class EventStatusInDB(EventStatusBase):
    id: int
    name_id: Optional[str]
    name: Optional[str]
    created_at: datetime


class EventStatusCreate(EventStatusBase):
    pass


class EventStatusUpdate(EventStatusBase):
    pass
