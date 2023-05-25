import datetime, pytz

we_are_here = datetime.datetime.now(tz=pytz.timezone('Europe/Kiev'))
print(we_are_here)
print(type(we_are_here))

hour_x = datetime.datetime(year=2022, month=11, day=27, hour=17, minute=50)
print(hour_x)

if we_are_here.hour == hour_x.hour:
    print(f'We are here now: {we_are_here}')

str_now_1 = we_are_here.strftime("%d/%m/%Y")
print(str_now_1)
str_now_2 = we_are_here.strftime("%A %d. %B %Y")
print(str_now_2)
my_time = we_are_here.strftime("%d %B %Y (%A) %H:%M:%S")
print(my_time)

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior - посилання на doc
# по форматуванню часу

