def prime(a):
    for i in range(a):
        if i == 0 or i == 1:
            continue
        if a % i == 0:
            return 0
    return a

def filter(a):
    y = lambda z : prime(z)
    return y(a)


l = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for x in l:
    if filter(x) != 0:
        print(x)