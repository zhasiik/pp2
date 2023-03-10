import os

path = str(input("path:"))

for item in os.listdir(path):
    print(item) 