import decimal
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


# --- API ---
class EventCreateAPI(BaseModel):
    coefficient: decimal.Decimal
    deadline_ts: datetime

    # deadline_ts - преобразовывается в datetime

    @field_validator('coefficient', mode='before')
    def must_two_decimals(cls, v):
        if '.' in str(v) and len(str(v).rsplit('.')[-1]) > 2:
            raise ValueError('must contain two decimals')
        return v


class EventCallback(BaseModel):
    id: int
    status_id: Optional[int]
    coefficient: decimal.Decimal
    deadline_dt: datetime
    updated_at: Optional[datetime]
    created_at: datetime
