def remove(string):
    return string.replace(" ", "")

def has_33(nums):
    if "33" in nums:
        return True
    else:
        return False   

a = input()
b = remove(a)
print(has_33(b))