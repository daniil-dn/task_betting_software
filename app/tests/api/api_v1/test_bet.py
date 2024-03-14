import asyncio
from datetime import datetime, timedelta

import pytz
import requests

from app.bet_maker.api.api_v1.endpoints.bet import bets
from app.core import settings
from app.models import Bet, BetStatus


class TestEvent:

    def test_create_bet(self) -> None:
        r = requests.get(
            f"http://app_bet_maker:9090{settings.API_V1_STR}/events"
        )
        assert r.status_code == 200
        events = r.json()
        if not events:
            data = {"coefficient": 1.22,
                    "deadline_ts": (datetime.now(tz=pytz.UTC) + timedelta(seconds=30)).timestamp()}
            r = requests.put(
                f"http://app_line_provider:9090{settings.API_V1_STR}/event", json=data
            )
            assert r.status_code == 200
            event = r.json()
        else:
            event = events[0]
        bet_data = {"event_id": event['id'], "amount": 1.22}
        r = requests.post(
            f"http://app_bet_maker:9090{settings.API_V1_STR}/bet",
            json=bet_data
        )
        assert r.status_code == 200

    def test_get_bets(self) -> None:
        r = requests.get(
            f"http://app_bet_maker:9090{settings.API_V1_STR}/bets"
        )
        assert r.status_code == 200

    def test_get_bets_mock(self) -> None:
        from mock import patch

        with patch('app.crud.crud_bet.get_all') as perm_mock_bet:
            perm_mock_bet.return_value = [
                Bet(id=1, event_id=1, status_id=1, amount=1, updated_at=datetime.now(), created_at=datetime.now()),
                Bet(id=1, event_id=1, status_id=1, amount=1, updated_at=datetime.now(), created_at=datetime.now()),
                Bet(id=1, event_id=1, status_id=1, amount=1, updated_at=datetime.now(), created_at=datetime.now()),
                Bet(id=1, event_id=1, status_id=1, amount=1, updated_at=datetime.now(), created_at=datetime.now())
            ]
            with patch('app.crud.crud_bet_status.get_all') as perm_mock_bet_statuses:
                perm_mock_bet_statuses.return_value = [
                    BetStatus(id=1, name='ещё не сыграла', created_at=datetime.now()),
                    BetStatus(id=2, name='Выиграла', created_at=datetime.now()),
                    BetStatus(id=3, name='Проиграла', created_at=datetime.now())]
                test_bets = asyncio.run(bets())
                print(test_bets)
                assert len(test_bets) == 4

    def test_get_events(self) -> None:
        r = requests.get(
            f"http://app_bet_maker:9090{settings.API_V1_STR}/events"
        )
        assert r.status_code == 200
