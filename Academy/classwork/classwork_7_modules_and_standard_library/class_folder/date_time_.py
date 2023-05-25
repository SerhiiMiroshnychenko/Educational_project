import datetime
import pytz


def return_datetime(date):
    return datetime.datetime.fromisoformat(date).astimezone(tz=pytz.UTC)


print(return_datetime(str(datetime.datetime.now(tz=pytz.timezone('Europe/Kyiv')))))
