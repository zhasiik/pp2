#6
def back_front(a):
    res = []
    for x in reversed(a):
        res.append(x)
    return res

a = input().split()

print(*back_front(a))