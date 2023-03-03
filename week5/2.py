
import re
txt = input()
x = re.findall("ab{2,3}", txt)
print(x)