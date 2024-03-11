import random
from datetime import datetime

import aio_pika
import pytz

from app.core import deps
from app.crud import crud_event
from app.db import SessionLocal
from app.line_provider.schemas import api_schemas
from app.line_provider.schemas.rq_tasks_schemas import ProcessEventTask
from app.logs import process_event_log
from app.models import Event
from app.schemas import crud_schemas


async def process_event(ctx: dict, message_in: ProcessEventTask):
    """Проводится обработка события и отправка коллбэка в реббит для bet_maker"""
    process_event_log.info(f'process event {message_in.event_id}')
    async with SessionLocal() as db:
        # получем событие
        event: Event = await crud_event.get_by_id(db, id=message_in.event_id)
        deadline_dt: datetime = event.deadline_dt

        # если событие не завершено и время его дедлайна прошло
        if deadline_dt <= datetime.now(tz=pytz.UTC) and event.status_id == 1:
            event: Event = await crud_event.lock_row(db, id=message_in.event_id)
            event_data = crud_schemas.EventUpdate(
                id=event.id,
                status_id=random.choice(message_in.status_ids)
            )
            event: Event = await crud_event.update(db, db_obj=event, obj_in=event_data)
    # отправляем коллбэк
    event_data = api_schemas.EventCallback(
        id=event.id, status_id=event.status_id, coefficient=event.coefficient,
        deadline_dt=event.deadline_dt, updated_at=event.updated_at,
        created_at=event.created_at
    )
    armq = await deps.get_armq()
    async with armq:
        channel = await armq.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(
                headers=None,
                body=event_data.model_dump_json().encode('utf-8')
            ),
            routing_key='event_callback',

        )
        await armq.close()
    process_event_log.info(f'END process_event {message_in.event_id}')
