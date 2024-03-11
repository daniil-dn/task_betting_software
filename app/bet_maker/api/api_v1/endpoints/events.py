import json
from typing import Any, List

import aiohttp
from fastapi import APIRouter

from app.bet_maker.schemas import api_schemas
from app.logs import server_log

# app

router = APIRouter()


@router.get("/events", response_model=List[api_schemas.EventGet])
async def events(
) -> Any:
    server_log.debug("Get all events")
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get("http://app_line_provider:9090/api/v1/events") as response:
            content: bytes = await response.content.read()
    return json.loads(content.decode('utf-8'))
