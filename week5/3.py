import re
txt = input()
l = []
txt = txt.split('_')
for i in range(0, len(txt) - 1):
    x1 = re.search("[a-z]", txt[i])
    x2 = re.search("[a-z]", txt[i + 1])
    if x1 and x2:
        l.append(txt[i] + "_" + txt[i + 1])
print(l)