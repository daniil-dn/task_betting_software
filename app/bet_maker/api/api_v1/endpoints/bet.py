import json
from datetime import datetime
from typing import Any, List

import aiohttp
import pytz
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.bet_maker.schemas import api_schemas
from app.core import deps
from app.crud import crud_bet, crud_bet_status
from app.schemas import crud_schemas

# app

router = APIRouter()


@router.post("/bet", response_model=api_schemas.BetGetResponseAPI)
async def bet(
        message_in: api_schemas.BetCreateAPI,
        db: AsyncSession = Depends(deps.get_db),
) -> Any:
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(f"http://app_line_provider:9090/api/v1/event/{message_in.event_id}") as response:
            content = await response.content.read()
            if response.status != 200:
                raise HTTPException(status_code=404, detail='Event not found')

    event_dict = json.loads(content.decode('utf-8'))
    event = crud_schemas.EventInDB(**event_dict)
    if event.status_id != 1 or event.deadline_dt < datetime.now(tz=pytz.UTC):
        raise HTTPException(status_code=400, detail='You cant bet on this event')
    bet_indb = await crud_bet.create(db, obj_in=crud_schemas.BetCreate(**message_in.model_dump(), status_id=1))
    return api_schemas.BetGetResponseAPI(**bet_indb.__dict__, status='ещё не сыграла')


@router.get("/bets", response_model=List[api_schemas.BetGetResponseAPI])
async def bets(
        db: AsyncSession = Depends(deps.get_db),
) -> Any:
    bet_statuses_db = await  crud_bet_status.get_all(db)
    bet_statuses_dict = {bet_status.id: bet_status.name for bet_status in bet_statuses_db}
    return [
        api_schemas.BetGetResponseAPI(**bet.__dict__, status=bet_statuses_dict[bet.status_id])
        for bet in await crud_bet.get_all(db)]
