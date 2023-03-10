import os

path = r"D:\pp2\week6\dir-and-files\44.txt"
file = open(path, "r")
lines = 0
for i in file:
    if(i != '\n'):
        lines += 1
print("Amount of lines in this file is:", lines)
