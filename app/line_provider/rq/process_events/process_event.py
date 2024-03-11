import random
from datetime import datetime

import aiohttp
import pytz

from app.crud import crud_event
from app.db import SessionLocal
from app.line_provider.schemas import api_schemas
from app.line_provider.schemas.rq_tasks_schemas import ProcessEventTask
from app.logs import process_event_log
from app.models import Event
from app.schemas import crud_schemas


async def process_event(ctx: dict, message_in: ProcessEventTask):
    process_event_log.info(f'process event {message_in.event_id}')
    async with (SessionLocal() as db):
        event: Event = await crud_event.get_by_id(db, id=message_in.event_id)
        deadline_dt: datetime = event.deadline_dt
        if deadline_dt <= datetime.now(tz=pytz.UTC) and event.status_id == 1:
            event: Event = await crud_event.lock_row(db, id=message_in.event_id)
            event_data = crud_schemas.EventUpdate(
                id=event.id,
                status_id=random.choice(message_in.status_ids)
            )
            event: Event = await crud_event.update(db, db_obj=event, obj_in=event_data)

    event_data = api_schemas.EventGet(
        id=event.id, status_id=event.status_id, coefficient=event.coefficient,
        deadline_dt=event.deadline_dt, updated_at=event.updated_at,
        created_at=event.created_at
    )
    url_get_event = "http://app_bet_maker:9090/api/v1/callback/process_event"
    async with aiohttp.ClientSession(
            trust_env=True
    ) as session:
        async with session.post(
                url_get_event,
                json=event_data.model_dump(mode='json')
        ) as response:
            if response.status != 200:
                process_event_log.error(response.content)
    process_event_log.info(f'END process_event {message_in.event_id}')
