import math

n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
apothem = s / (math.tan(math.pi / n) * 2)

print("The area of the polygon is: ", round((n * s * apothem) / 2))