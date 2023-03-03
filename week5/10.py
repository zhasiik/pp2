import re
global txt
txt = input()
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
    txt = txt[:pos] + "_" + txt[pos].lower() + txt[pos+1:]
print(txt)