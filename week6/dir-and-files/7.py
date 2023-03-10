import os

path1 = r"D:\pp2\week6\dir-and-files\44.txt"
path2 = r"D:\pp2\week6\dir-and-files\77.txt"

file1 = open(path1, "r")
file2 = open(path2, 'w')

file2.write(file1.read())

file1.close()
file2.close()