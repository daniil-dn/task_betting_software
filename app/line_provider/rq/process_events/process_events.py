from datetime import datetime

import pytz

from app.crud import crud_event
from app.crud import crud_event_status
from app.db import SessionLocal
from app.line_provider.schemas.rq_tasks_schemas import ProcessEventTask
from app.logs import process_event_log
from app.schemas import crud_schemas


async def process_events(ctx: dict):
    process_event_log.info('Process Events')
    async with SessionLocal() as db:
        events_statuses: list[crud_schemas.EventStatusInDB] = await crud_event_status.get_all(db)
        status_ids: list[int] = [status.id for status in events_statuses
                                 if status.name_id != 'not_finished']
        events: list[crud_schemas.EventInDB] = await crud_event.get_all_not_processed(db)
        for event in events:
            process_event_log.info(f'Send PROCESS EVENT Task: {event.id}')
            deadline_dt: datetime = event.deadline_dt
            if deadline_dt <= datetime.now(tz=pytz.UTC):
                await ctx['redis'].enqueue_job(
                    'process_event',
                    message_in=ProcessEventTask(event_id=event.id, status_ids=status_ids),
                    _queue_name="process_events_tasks"
                )
    process_event_log.info('END Process Events')
