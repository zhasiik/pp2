n = int(input())
x = (i ** 2 for i in range(n))

for i in range(n):
    print(next(x))