import re
txt = input()
x = re.findall("[A-Z][a-z]+", txt)
print(x)