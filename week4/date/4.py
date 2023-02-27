import datetime

d1 = datetime.date.today()
d2 = d1 - datetime.timedelta(days = 5)
d3 = d1 - d2

print(d3.total_seconds())