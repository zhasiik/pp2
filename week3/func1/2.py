def to_Celcius(Fahrenheit : int):
    return((5 / 9) * (Fahrenheit - 32))

Fahrenheit = int(input())

print(to_Celcius(Fahrenheit), "°C")