import decimal

from pydantic import BaseModel, field_validator


class BetBase(BaseModel):
    pass


# --- API ---
class BetCreateAPI(BetBase):
    event_id: int
    amount: decimal.Decimal

    @field_validator('amount', mode='before')
    def must_two_decimals(cls, v):
        if len(str(v).rsplit('.')[-1]) > 2:
            raise ValueError('must contain two decimals')
        return v
