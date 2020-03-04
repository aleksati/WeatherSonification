import datetime
from pytz import timezone

# Get time from different timezones. Format = daymonthhourminute
def time(zone):
    now = datetime.datetime.now(timezone(zone))
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")

    timeatplace = day + month + hour + minute
    return timeatplace


print(time('CET'))