import time

x = int(input("Write number:"))
delay = int(input("Write microsec:"))

time.sleep(delay / 1000)

print("Square root of {} after {} miliseconds is {}".format(x, delay, pow(x, 0.5)))