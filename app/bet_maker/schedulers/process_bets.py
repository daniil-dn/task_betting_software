import json

import aiohttp

from app.crud import crud_bet
from app.db import SessionLocal
from app.logs import scheduler_log
from app.schemas import crud_schemas


async def process_bets():
    # todo воркер arq
    async with SessionLocal() as db:
        scheduler_log.info('PROCESS BETS')
        bets = await crud_bet.get_all_not_processed(db)
        for bet in bets:
            async with aiohttp.ClientSession(trust_env=True) as session:
                async with session.get(
                        f"http://app_line_provider:9090/api/v1/event/{bet.event_id}"
                ) as response:
                    content = await response.content.read()
                    if response.status != 200:
                        scheduler_log.error(f'Event error: {content}')
                        return
            event_dict = json.loads(content.decode('utf-8'))
            event = crud_schemas.EventInDB(**event_dict)
            scheduler_log.info(f'Event status bet:{bet.id} event:{event.id}')
            if event.status_id == 2:
                bet_status = 2
            elif event.status_id == 3:
                bet_status = 3
            else:
                return

            bet_data = crud_schemas.BetUpdate(id=bet.id, status_id=bet_status)
            await crud_bet.update(db, db_obj=bet, obj_in=bet_data)

    scheduler_log.info('END PROCESS BETS')
