#4
def check_prime(x):
    if x==1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def filter_primes(a):
    res = []
    for i in a :
        if check_prime(i)==True:
            res.append(i)
    return res

a = input().split()
b = []

for x in a : 
    b.append(int(x))

print(filter_primes(b)) 