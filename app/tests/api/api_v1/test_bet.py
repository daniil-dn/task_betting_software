from datetime import datetime, timedelta

import pytz
import requests

from app.core import settings


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

    def test_get_events(self) -> None:
        r = requests.get(
            f"http://app_bet_maker:9090{settings.API_V1_STR}/events"
        )
        assert r.status_code == 200
