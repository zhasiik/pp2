#13
import random
x=(random.randrange(1,20))
print("Hello! What is your name?")

a=input()
print()
myname = "Well, {}, I am thinking of a number between 1 and 20."    
print(myname.format(a))
print("Take a guess.")
b = int(input())
cnt = 1
while b!=x:
    cnt+=1
    if  b < x:
        print("Your guess is too low.")
        print("Take a guess.")
    if b > x:
        print("Your guess is too up.")
        print("Take a guess.")
    b = int(input())
    
print('Good job, ' + str(a) +  '! You guessed my number in '+ str(cnt)+ ' guesses!')