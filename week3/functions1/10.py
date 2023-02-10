def new_list(odd):
    new = []
    for x in odd :
        if x not in new:
            new.append(x)
    return new

a = input().split()
print(new_list(a))