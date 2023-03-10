a = input()

print(sum(x.islower() for x in a))
print(sum(x.isupper() for x in a))