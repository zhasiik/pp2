def is_palindrome(a):
    return list(reversed(a)) == list(a)

a = input()
print(is_palindrome(a))