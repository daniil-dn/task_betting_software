from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import deps
from app.crud import crud_event
from app.line_provider.schemas import api_schemas
from app.schemas import crud_schemas

# app

router = APIRouter()


@router.put('/event', response_model=crud_schemas.EventInDB)
async def create_event(
        message_in: api_schemas.EventCreateAPI,
        db: AsyncSession = Depends(deps.get_db)
):
    # message_in.deadline_ts - уже переведо из timestamp -> datetime
    event_data = crud_schemas.EventCreate(
        coefficient=message_in.coefficient, deadline_dt=message_in.deadline_ts, status_id=1
    )
    return await crud_event.create(db, obj_in=event_data)


@router.get('/event/{event_id}', response_model=crud_schemas.EventInDB)
async def get_event(event_id: int, db: AsyncSession = Depends(deps.get_db)):
    event = await crud_event.get_by_id(db, id=event_id)
    if not event:
        raise HTTPException(status_code=404, detail='Event not found')
    return event


@router.get('/events', response_model=List[crud_schemas.EventInDB])
async def get_events(db: AsyncSession = Depends(deps.get_db)):
    return await crud_event.get_all_can_bet(db)
