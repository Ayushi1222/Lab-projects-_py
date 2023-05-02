import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("*Length of the password you need should be minimum 8 and maximum 12. ")
nr_letters= int(input("How many letters(alphabets) would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passcode = ''
for i in range(nr_letters):
  passcode = passcode + random.choice(letters)
for i in range(nr_numbers):
  passcode = passcode + random.choice(numbers)
for i in range(nr_symbols):
  passcode = passcode + random.choice(symbols)  
Ur_password = ''.join(random.sample(passcode,len(passcode)))
if len(Ur_password)<8:
    p_word=''.join(random.choices(letters,k=8-len(Ur_password)))
    Ur_password+=p_word
print(Ur_password)    
