import re
ababa = input()
a = re.findall("ab*", ababa)
print(a)
