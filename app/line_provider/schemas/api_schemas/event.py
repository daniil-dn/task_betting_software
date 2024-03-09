import decimal

from pydantic import BaseModel, field_validator


class EventBase(BaseModel):
    pass


# --- API ---
class EventCreateAPI(EventBase):
    coefficient: decimal.Decimal
    deadline_ts: int

    @field_validator('coefficient', mode='before')
    def must_two_decimals(cls, v):
        if len(str(v).rsplit('.')[-1]) > 2:
            raise ValueError('must contain two decimals')
        return v
