import datetime

import pytz
import requests

from app.core import settings


class TestEvent:
    def test_create_get_event(self) -> None:
        data = {"coefficient": 1.22,
                "deadline_ts": (datetime.datetime.now(tz=pytz.UTC)).timestamp()}
        r = requests.put(f"http://app_line_provider:9090{settings.API_V1_STR}/event", json=data)
        print(r.content)
        assert r.status_code == 200
        r = requests.get(f"http://app_line_provider:9090{settings.API_V1_STR}/event/{r.json()['id']}")
        assert r.status_code == 200

    def test_get_all_events(self) -> None:
        r = requests.get(f"http://app_line_provider:9090{settings.API_V1_STR}/events")
        assert r.status_code == 200
