from itertools import permutations


def per(s):
    ans=list(permutations(s))
    for i in ans:
        print(str().join(i),end=" ")
s = input()
print(per(s))