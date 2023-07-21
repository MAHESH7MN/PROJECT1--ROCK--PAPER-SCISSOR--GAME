import random

print(
  "*~*~*~*~*~**~*~*WELCOME TO THE GAME ROCK PAPER SCISSOR*~*~*~*~*~*~*~*~*")
print()
USER_SCORE = 0
COMPUTER_SCORE = 0
TIE = 0

NAME = input("please enter your name buddy! 🥷🙋‍♂️")

print('''
🏹GAME RULES ARE!🏹:
1. paper🧻  Vs rock🪨   -*-*-*-*-*->paper Win's!🧻
2. rock🪨   Vs scissor✂️-*-*-*-*-*->rock Win's! 🪨
3. scissor✂️Vs paper🧻  -*-*-*-*-*->scissor Win's!✂️
''')
print()
while True:
  CHOICE = int(input("please enter your choice from 1-3:"))
  print()
  while CHOICE > 3 or CHOICE < 1:
    CHOICE = int(input("please enter valid input from 1-3"))

  if CHOICE == 1:
    user_choice = "rock🪨"
  elif CHOICE == 2:
    user_choice = "paper🧻"
  else:
    user_choice = "scissor✂️"
  print()
  print(NAME, "choice is 🙋‍♀️", user_choice)
  print("Now it's computer turn💻")
  print()
  computer = random.randint(1, 3)

  if computer == 1:
    computer_choice = "rock🪨"
  elif computer == 2:
    computer_choice = "paper🧻"
  else:
    computer_choice = "scissor✂️"
  print()
  print("💻computer choice is", computer_choice)

  if (user_choice == "paper🧻"
      and computer_choice == "rock🪨") or (user_choice == "rock🪨"
                                          and computer_choice == "paper🧻"):
    print("paper🧻 Win's")
    Result = "paper🧻"
  elif (user_choice == "rock🪨" and computer_choice == "scissor✂️") or (
      user_choice == "scissor✂️" and computer_choice == "rock🪨"):
    print("rock🪨 Win's")
    Result = "rock🪨"
  elif (user_choice == computer_choice):
    print("its a Tie😒")
    Result = "Tie😒"
  else:
    print("scissor✂️ Win's")
    Result = "scissor✂️"

  if Result == "Tie😒":
    print("GAME Tie😒")
    TIE += 1
  elif Result == user_choice:
    print(NAME, "WIN'S🤩")
    USER_SCORE += 1
  else:
    print("COMPUTER Win's🤪")
    COMPUTER_SCORE += 1
  print()
  print("Scores are:")
  print(NAME, "🥷Score is:", USER_SCORE)
  print("💻computer Score is:", COMPUTER_SCORE)
  print("😒tie's are:", TIE)
  print()
  repeat = input("🥷 🦹Do you challenge me again🥷")
  if repeat == "yes" and repeat == "YES":
    CHOICE = int(input("let's play"))
  elif repeat != "YES" and repeat != "yes" and repeat != "no" and repeat != "NO":
    repeat = input("please enter valid command Yes or NO")

  elif repeat != "yes" and repeat != "YES" and repeat != "no" and repeat != "NO":
    print("Invalid command🫥")
    repeat = input("😀 Please enter valid command yes or no 😀 ")
    if repeat=="yes" or repeat=="YES":
       CHOICE=int(input(" please enter your choice from 1-2"))
    else:
       repeat=input(str("Please enter valid command yes or no"))

  elif repeat == "no" or repeat == "NO":
    break
  print()
if COMPUTER_SCORE > USER_SCORE:
  print("The winners is computer💻 ")
elif USER_SCORE > COMPUTER_SCORE:
  print("The winner is ", NAME)
elif USER_SCORE == COMPUTER_SCORE == TIE:
  print("Match are Tie😒")
else:
  print("Match are Tie😒")

print("👋Game over👋")
print("Well play 👏", NAME)
print(" 💐 Thank u for playing 💐 ")
