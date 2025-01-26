# /usr/bin/python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import datetime


def get_future_time(hours: int, minutes: int, add_minutes: int) -> datetime.datetime:
    """
    Get future time
    :param hours: hours
    :param minutes: minutes
    :param add_minutes: add minutes
    :return: future time
    """
    now = datetime.datetime.now()
    future_time = now.replace(hour=hours, minute=minutes, second=0,
                              microsecond=0) + datetime.timedelta(minutes=add_minutes)
    return future_time
