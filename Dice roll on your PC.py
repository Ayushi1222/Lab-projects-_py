import random
ls=[]
print('WELCOME TO YOUR ONLINE DICE ROLL!')
n=int(input("Enter the number of dice you want to roll at a time: "))
for i in range(n):
    a=random.randint(1,6)
    ls.append(a)
print(ls) 
