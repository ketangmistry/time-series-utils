import pytest
import datetime
from src.datetime_utils import get_future_time

def test_get_future_time():
    now = datetime.datetime.now()
    future_time = get_future_time(now.hour, now.minute, 30)
    expected_time = now.replace(second=0, microsecond=0) + datetime.timedelta(minutes=30)
    assert future_time == expected_time

    future_time = get_future_time(23, 45, 30)
    expected_time = now.replace(hour=23, minute=45, second=0, microsecond=0) + datetime.timedelta(minutes=30)
    assert future_time == expected_time

    future_time = get_future_time(1, 2, 732)
    expected_time = now.replace(hour=1, minute=2, second=0, microsecond=0) + datetime.timedelta(minutes=732)
    assert future_time == expected_time