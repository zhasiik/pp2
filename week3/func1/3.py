rabbit = int()
chicken = int()

def my_function(numheads, numlegs):
    numheads = numheads * 2 
    numlegs = numlegs - numheads  
    rabbit = numlegs / 2 
    numheads = numheads / 2   
    chicken = numheads - rabbit   
    print (rabbit, chicken)
    

x = int(input())
y = int(input())
my_function(x, y)

"""
def solve(h, l):
    c = 1
    while l - c * 2 != (h - c) * 4:
        c += 1
    return (c, h - c)

print(solve(35, 94))
"""