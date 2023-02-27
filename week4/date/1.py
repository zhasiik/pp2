import datetime

today = datetime.datetime.now()
delta = datetime.timedelta(days = 5)

print(today - delta)