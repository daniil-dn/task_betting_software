import asyncio

from app.crud import crud_bet_status, crud_event_status
from app.db import SessionLocal
from app.logs import server_log
from app.models import EventStatus, BetStatus
from app.schemas import crud_schemas


async def fill_db():
    async with SessionLocal() as db:
        server_log.info('FILL DB')
        events_statuses: list[EventStatus] = await crud_event_status.get_all(db)
        bets_statuses: list[BetStatus] = await crud_bet_status.get_all(db)
        if not events_statuses:
            await crud_event_status.create(
                db, obj_in=crud_schemas.EventStatusCreate(
                    id=1, name_id='not_finished', name='Незавершённое'
                )
            )
            await crud_event_status.create(
                db, obj_in=crud_schemas.EventStatusCreate(
                    id=2, name_id='first_win', name='Завершено выигрышем первой команды'
                )
            )
            await crud_event_status.create(
                db, obj_in=crud_schemas.EventStatusCreate(
                    id=3, name_id='second_win', name='Завершено выигрышем второй команды'
                )
            )
        if not bets_statuses:
            await crud_bet_status.create(
                db, obj_in=crud_schemas.BetStatusCreate(
                    id=1, name_id='not_finished', name='ещё не сыграла'
                )
            )
            await crud_bet_status.create(
                db, obj_in=crud_schemas.EventStatusCreate(
                    id=2, name_id='win', name='выиграла'
                )
            )
            await crud_bet_status.create(
                db, obj_in=crud_schemas.EventStatusCreate(
                    id=3, name_id='lose', name='проиграла'
                )
            )


if __name__ == "__main__":
    asyncio.run(fill_db())
