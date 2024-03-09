import random
from datetime import datetime

import pytz

from app.crud import crud_event
from app.crud import crud_event_status
from app.db import SessionLocal
from app.logs import scheduler_log
from app.schemas import crud_schemas


async def process_events():
    # todo воркер arq
    scheduler_log.info('PROCESS EVENTS')
    async with SessionLocal() as db:
        events_statuses = await crud_event_status.get_all(db)
        status_ids = [status.id for status in events_statuses if status.name_id != 'not_finished']
        events = await crud_event.get_all_not_processed(db)
        for event in events:
            deadline_dt = event.deadline_dt
            if deadline_dt <= datetime.now(tz=pytz.UTC):
                event_data = crud_schemas.EventUpdate(id=event.id, status_id=random.choice(status_ids))
                await crud_event.update(db, db_obj=event, obj_in=event_data)
    scheduler_log.info('END PROCESS EVENTS')
