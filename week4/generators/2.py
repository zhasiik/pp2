n = int(input())
x = (i for i in range(0, n + 1, 2))

for i in range(int(n / 2)):
    print(next(x), end = ", ")
print(next(x))