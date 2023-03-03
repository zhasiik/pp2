import re
txt = input()
x = txt
for i in range(0, len(x)):
    if x[i].isupper():
        x1 = x[:i]
        x2 = x[i + 1:]
        x = x1 + ' ' + x2
l = x.split(' ')
l2 = []
for i in l:
    if len(i) != 0:
        l2.append(i)
print(l2)