# fastapi
import asyncio
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

# app config
from app.bet_maker.api.api_v1.api import api_router
from app.bet_maker.schedulers import process_bets
from app.core.config import settings
# app services
from app.logs import server_log
from app.metrics_prometheus import instrumentator

server_log.info(f'Sentry is ON. Debug Mode is {settings.DEBUG}')
scheduler = AsyncIOScheduler({'event_loop': asyncio.get_event_loop()})
scheduler.add_job(process_bets, 'interval', seconds=30, next_run_time=datetime.now())
scheduler.start()

# Запуск приложения. При запуске стартует клиент ТГ и при выключении происходит диссконнект клиента
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",
    on_startup=[], on_shutdown=[]
)
instrumentator.instrument(app).expose(app)
app.include_router(api_router, prefix=settings.API_V1_STR)
server_log.info('CREATE FASTAPI APP')
