rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
l = [rock, paper, scissors]
print(f'''Lets play ROCK,PAPER,SCISSORS exploiter ;)
Rules of the Game:---
a)ROCK beats SCISSORS.
b)SCISSORS beats PAPER.
c)PAPER beats ROCK.

(Get ready to lose XD)
''')
while(1):
    index1 = int(input("Enter your choice rock(0),paper(1),scissors(2)....-:"))
    p1 = l[index1]
    print("Your choice-:")
    print(p1)
    index2 = random.randint(0, 2)
    p2 = l[index2]
    print("Computer's choice-:")
    print(p2)
    if (index1 == 0 and index2 == 2) or (index1 == 1 and index2 == 0) or (index1 == 2 and index2 == 1):
        print("............You won..............")
    elif (index1 == 2 and index2 == 0) or (index1 == 0 and index2 == 1) or (index1 == 1 and index2 == 2):
        print("............You lost.............")
    else:
        print("Draw")
    a=input("One more try? Enter 'y' to play again or 'n' to stop. ")
    if a=='y':
        continue
    else:
        break
