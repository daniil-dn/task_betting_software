from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.bet_maker.schemas import api_schemas
from app.core import deps
from app.crud import crud_bet
from app.schemas import crud_schemas

router = APIRouter()


@router.post("/process_event")
async def process_event(
        message_in: api_schemas.EventGet,
        db: AsyncSession = Depends(deps.get_db),
) -> Any:
    bets_with_event = await crud_bet.get_by_event_id(db, event_id=message_in.id)
    for bet in bets_with_event:
        bet_status = 1
        if message_in.status_id == 2:
            bet_status = 2
        elif message_in.status_id == 3:
            bet_status = 3

        await crud_bet.update(db, db_obj=bet, obj_in=crud_schemas.BetUpdate(id=bet.id, status_id=bet_status))
