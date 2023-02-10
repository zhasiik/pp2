def histo(b):
    res = []
    for x in b:
        res.append("*"*x)
    return res

a = input().split()
b = []

for x in a : 
    b.append(int(x))

print(*(histo(b)), sep = "\n")