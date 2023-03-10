import os

path = r"D:\pp2\week6\dir-and-files\55.txt"

mylist = ["Python", "is", "so", "interesting"]
file = open(path, "w")
for i in mylist:
    file.write(i + ' ')
file.close()

file = open(path, "r")
print(file.read())