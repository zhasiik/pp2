def check(a):
    reverse = a[::-1]
    if reverse == a:
        return True
    else : 
        return False

a = str(input())
b = a[::-1]
print(check(a))