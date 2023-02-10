#8
def to_string(nums):
    mystring = ''
    for x in nums:
        mystring += x   
    return mystring

def check(mystring):
    if "007" in mystring:
        return True
    else:
        return False

a = input().split()
b = []  
for x in a :
    if x == "0":
        b.append("0")
    if x == "7":
        b.append("7")
c = to_string(b)
print(check(c))