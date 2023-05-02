import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
word_dict = {"introvert":"Person who is less social.","phone":"Thing Gen-Z can't live without","starbucks":"Most show offed thing on people's stories","vrindavan":"Place of devotion and faith","confidence":"Another word for self-esteem","clouds":"Best thing to admire in rainy season","time":"Key to success"}
ls = list(word_dict.items())
n=random.randint(0,len(ls))
chosen_word,hint=ls[n]
lives=6
display = []
print('''SAVE!!SAVE!!SAVE!!
Save your man from being hang 😖😖
All you have to do is, guess the letters of the given words without losing lives
You have 6 lives.
''')
for _ in range(len(chosen_word)):
    display += "_"
print(display)
print(f"Hint:{hint}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i]== guess:
            display[i] = chosen_word[i]
    if guess not in chosen_word:
      lives-=1
      if lives==0:
        end_of_game=True
        print("You lose＞﹏＜.")
        print(f"The word was {chosen_word}.")
      if lives!=0:
          print(f"{' '.join(display)}")
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You winㄟ(≧◇≦)ㄏ.")
