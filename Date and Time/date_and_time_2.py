# Computing Time Differences

"""
    The timedelta module comes in handy to compute differences between times.
"""
from datetime import datetime, timedelta

now = datetime.now()
then = datetime(2016, 5, 23)

dif = now - then
#dif is of type timedelta
print(dif.days)
print(dif.seconds)

# To get n day's after and n day's before date we could use a function as following

def get_n_days_after_date(date_format="%d %B %Y", add_days=120):
    date_n_days_after = datetime.now() + timedelta(days=add_days)
    return date_n_days_after

def get_n_days_before_date(date_format= "%d %B %Y", days_before=120 ):
    date_n_dats_ago = datetime.now() - timedelta(days=days_before)
    return date_n_dats_ago.strftime(date_format)

print()
"""
    Switching between time zones
        to switch between time zones, you need datetime objects that are timezone-aware
"""
from dateutil import tz

utc = tz.tzutc()
local = tz.tzlocal()

utc_now = datetime.utcnow()
print(utc_now)

utc_now = utc_now.replace(tzinfo=utc)
print(utc_now)

local_now = utc_now.astimezone(local)
print(local_now)

"""
    Simple Date arithmetic
        Dates don't exist in isolation. It is common that yyou will need to find the amount of time
        between dates or determine what the date will be tomorrow. This can be accomplished using
        timedelta objects.
"""

import datetime

today = datetime.date.today()
print("Today: ", today)

yesterday = today-datetime.timedelta(days=1)
print("Yesterday: ", yesterday)

tomorrow = today+datetime.timedelta(days=1)
print("Tomorrow: ", tomorrow)

print("Time between tomorrow and yesterday: ", tomorrow-yesterday)

print()
"""
    Iterate Over dates
        Sometimes you want to iterate over a range of dates froma start date to some end date.
        You can do it using datetime library and timedelta object:
"""

#The size of each step in days
day_delta = datetime.timedelta(days=1)

start_date = datetime.date.today()
end_date = start_date+ 7*day_delta

# Loop over the date
for i in range((end_date-start_date).days):
    print(start_date+i*day_delta)