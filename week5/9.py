import re
global txt
global txt1
txt = input()
txt1 = txt
global x
x = True
global cal
cal = 0
while x:
    x = re.search("[A-Z]", txt)
    if x == None:
        break
    p = x.span()
    pos = p[0]
    txt = txt[:pos] + txt[pos].lower() + txt[pos+1:]
    if pos == 0:
        continue
    pos += cal
    cal += 1
    txt1 = txt1[:pos] + " " + txt1[pos:]
print(txt1)