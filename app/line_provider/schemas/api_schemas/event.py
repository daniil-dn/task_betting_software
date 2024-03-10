import decimal
from datetime import datetime

from pydantic import BaseModel, field_validator


class EventBase(BaseModel):
    pass


# --- API ---
class EventCreateAPI(EventBase):
    coefficient: decimal.Decimal
    deadline_ts: datetime

    @field_validator('coefficient', mode='before')
    def must_two_decimals(self, v):
        if '.' in str(v) and len(str(v).rsplit('.')[-1]) > 2:
            raise ValueError('must contain two decimals')
        return v
