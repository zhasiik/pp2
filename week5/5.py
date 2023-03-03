import re
txt = input()
x = re.findall("a.*b", txt)
print(x)