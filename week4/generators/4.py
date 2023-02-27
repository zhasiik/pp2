a = int(input())
b = int(input())
squares = (i * i for i in range(a, b + 1))


for x in squares:
    print(x, end = ' ')