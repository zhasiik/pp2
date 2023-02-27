import datetime

d1 = str(datetime.datetime.now())
d1 = d1.split(".")

print(d1[0])

d1 = datetime.datetime.now()
print(d1.strftime("%Y-%m-%d %H:%M:%S"))