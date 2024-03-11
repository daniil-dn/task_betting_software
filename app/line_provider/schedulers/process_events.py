import random
from datetime import datetime

import aiohttp
import pytz

from app.crud import crud_event
from app.crud import crud_event_status
from app.db import SessionLocal
from app.line_provider.schemas import api_schemas
from app.logs import scheduler_log
from app.schemas import crud_schemas


async def process_events():
    # todo воркер arq
    scheduler_log.info('PROCESS EVENTS')
    async with SessionLocal() as db:
        events_statuses: list[crud_schemas.EventStatusInDB] = await crud_event_status.get_all(db)
        status_ids: list[int] = [status.id for status in events_statuses
                                 if status.name_id != 'not_finished']
        events: list[crud_schemas.EventInDB] = await crud_event.get_all_not_processed(db)
        for event in events:
            deadline_dt: datetime = event.deadline_dt
            if deadline_dt <= datetime.now(tz=pytz.UTC):
                event_data = crud_schemas.EventUpdate(
                    id=event.id,
                    status_id=random.choice(status_ids)
                )
                event = await crud_event.update(db, db_obj=event, obj_in=event_data)
                url_get_event = f"http://app_bet_maker:9090/api/v1/callback/process_event"
                event_data = api_schemas.EventGet(
                    id=event.id, status_id=event.status_id, coefficient=event.coefficient,
                    deadline_dt=event.deadline_dt, updated_at=event.updated_at,
                    created_at=event.created_at
                )
                async with aiohttp.ClientSession(trust_env=True) as session:
                    async with session.post(url_get_event, json=event_data.model_dump(mode='json')) as response:
                        if response.status != 200:
                            scheduler_log.error(response.content)
    scheduler_log.info('END PROCESS EVENTS')
