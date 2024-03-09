# fastapi
from fastapi import FastAPI

from app.core.config import settings
# app config
from app.line_provider.api.api_v1.api import api_router
# app services
from app.logs import server_log
from app.metrics_prometheus import instrumentator

server_log.info(f'Sentry is ON. Debug Mode is {settings.DEBUG}')

# Запуск приложения. При запуске стартует клиент ТГ и при выключении происходит диссконнект клиента
app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",
    on_startup=[], on_shutdown=[]
)
instrumentator.instrument(app).expose(app)
app.include_router(api_router, prefix=settings.API_V1_STR)
server_log.info(f'CREATE FASTAPI APP')
