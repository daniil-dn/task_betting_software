import decimal
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# --- API ---
class EventGet(BaseModel):
    id: int
    status_id: Optional[int]
    coefficient: decimal.Decimal
    deadline_dt: datetime
    updated_at: Optional[datetime]
    created_at: datetime
