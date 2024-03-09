from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import deps
from app.crud import crud_event
from app.schemas import api_schemas, crud_schemas

# app

router = APIRouter()


@router.put('/event')
async def create_event(message_in: api_schemas.EventCreateAPI, db: AsyncSession = Depends(deps.get_db)):
    await crud_event.create(db, obj_in=message_in)


@router.get('/event/{event_id}')
async def get_event(event_id: int, db: AsyncSession = Depends(deps.get_db)):
    pass


@router.get('/events')
async def get_events(db: AsyncSession = Depends(deps.get_db)):
    pass
