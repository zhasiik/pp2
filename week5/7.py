import re
txt = input()
x = txt.split("_")
for i in range(1, len(x)):
    x[i] = x[i].capitalize()
for x in x:
    print(x, end='')