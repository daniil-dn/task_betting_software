from datetime import datetime
from typing import List

import pytz
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
# app
from app.models import Event
from app.schemas import crud_schemas


class CRUDEvent(
    CRUDBase[
        Event,
        crud_schemas.EventCreate,
        crud_schemas.EventUpdate]
):
    async def get_all_not_processed(
            self, db: AsyncSession
    ) -> List[Event]:
        q = select(Event).filter(Event.status_id == 1)
        res = await db.execute(q)
        return res.scalars().all()

    async def get_all_can_bet(
            self, db: AsyncSession
    ) -> List[Event]:
        q = select(Event).filter(
            Event.deadline_dt >= datetime.now(tz=pytz.UTC),
            Event.status_id == 1
        )
        res = await db.execute(q)
        return res.scalars().all()


crud_event = CRUDEvent(Event)
