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
