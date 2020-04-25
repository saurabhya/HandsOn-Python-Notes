# Parsing a string into a timezone aware datetime object

import datetime

dt = datetime.datetime.strptime("2020-04-25T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)

# Constructing timezone-aware datetimes
"""
    By default all datetime objects are naive. To make them timezone-aware, you must attach a tzinfo object,
    which provides the UTC offset and timezone abbriviation as a function of date and time.

    Fixed offset time zones
        For time zones that are fixed offset from UTC, in Python 3.2+, the datetime module provides the timezone class,
        a concrete implemenatation of tzinfo, which takesa timedelta and an(optional) name parameter
"""

from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9))

dt = datetime(2020, 1, 1, 12, 0, 0, tzinfo=JST)
print(dt)
print(dt.tzname())
print(dt.tzinfo)

dt = datetime(2020, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9),'JST'))
print(dt.tzname)

print()
"""
    All edge cases are handled properly when using pytz, but pytz time zones should not be directly attached to time
    zones through the constructor. Instead, a pytz time zone should be attached using the time zones's localize method.
"""
import pytz

PT = pytz.timezone('US/Pacific')
dt_pst = PT.localize(datetime(2020, 1, 1, 12))
dt_pdt = PT.localize(datetime(2020, 11, 1, 0, 30))

print(dt_pst)
print(dt_pdt)