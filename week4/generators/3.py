def func(n):
    def div(y):
        if y % 3 == 0 and y % 4 == 0:
            return y
    x = (div(i) for i in range(n + 1))
    return x

n = int(input())
x = func(n)
for i in x:
    if i != None:
        print(i)