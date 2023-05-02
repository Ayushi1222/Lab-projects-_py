import random
print(f'''----------WELCOME TO MASTER'S GUESS----------
*If you manage to choose the same number
as your partner(computer mahashye ji) you win...
*You will loose otherwise
----------GIVE IT A TRY,BEST OF LUCK---------
          ''')
x=random.randint(1,10)
while(1):
    y=int(input("Enter a number between 1 to 10: "))
    if x==y:
        print(f"{y} is your lucky number.You made it!!!")
        break
    else:
        print("Try again..")
        continue
