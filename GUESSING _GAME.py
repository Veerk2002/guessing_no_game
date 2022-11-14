       # SIMPLE GUESSING NUMBER GAME WITHIN COMPUTER AND USER


import random 
cnum=random.randrange(1,10)
userinput=int(input("enter your num "))
if userinput>cnum:
    print(cnum,"number")
    print("'your guess num is to high ")
elif cnum>userinput:
    print(cnum,("number"))
    print("your guess num is too low")
else:
    print(cnum)
    print("your guess no is equal")
