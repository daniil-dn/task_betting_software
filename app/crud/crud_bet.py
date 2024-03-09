from app.crud.base import CRUDBase
# app
from app.models import Bet
from app.schemas import crud_schemas


class CRUDBet(CRUDBase[Bet, crud_schemas.BetCreate, crud_schemas.BetUpdate]):
    pass


crud_bet = CRUDBet(Bet)
