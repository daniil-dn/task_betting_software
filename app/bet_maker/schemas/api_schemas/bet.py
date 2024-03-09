import decimal
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class BetBase(BaseModel):
    pass


# --- API ---
class BetCreateAPI(BetBase):
    event_id: int
    amount: decimal.Decimal

    @field_validator('amount', mode='before')
    def must_two_decimals(cls, v):
        if '.' in str(v) and len(str(v).rsplit('.')[-1]) > 2:
            raise ValueError('must contain two decimals')
        return v


class BetGetResponseAPI(BetBase):
    id: int
    event_id: int
    status: str
    amount: decimal.Decimal
    updated_at: Optional[datetime] = None
    created_at: datetime
