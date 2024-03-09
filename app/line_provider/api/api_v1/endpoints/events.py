from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import deps
from app.crud import crud_event
from app.line_provider.schemas import api_schemas
from app.schemas import crud_schemas

# app

router = APIRouter()


@router.put('/event')
async def create_event(message_in: api_schemas.EventCreateAPI, db: AsyncSession = Depends(deps.get_db)):
    await crud_event.create(db, obj_in=crud_schemas.EventCreate(**message_in.model_dump()))


@router.get('/event/{event_id}', response_model=crud_schemas.EventInDB)
async def get_event(event_id: int, db: AsyncSession = Depends(deps.get_db)):
    return await crud_event.get_by_id(db, id=event_id)


@router.get('/events', response_model=List[crud_schemas.EventInDB])
async def get_events(db: AsyncSession = Depends(deps.get_db)):
    return await crud_event.get_all(db)
