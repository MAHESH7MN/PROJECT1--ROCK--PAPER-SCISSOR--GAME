import random

dic = {
  "rock": "🪨",
  "paper": "🧻",
  "scissor": "✂️",
}
player_score = 0
computer_score = 0
tie = 0
print("welcome to the game🤝 - rock🪨,paper🧻,scissor✂️")
print('''
🏹GAME RULES ARE!🏹:
1. paper🧻  Vs rock🪨   -*-*-*-*-*->paper Win's!🧻
2. rock🪨   Vs scissor✂️-*-*-*-*-*->rock Win's! 🪨
3. scissor✂️Vs paper🧻  -*-*-*-*-*->scissor Win's!✂️
''')
NAME = input("\nPLEASE ENTER YOUR NAME BUDDY\n:-")

while True:
  player_turn = input("\n enter your choice(rock🪨,paper🧻,scissor✂️?) :- ")
  while player_turn != "rock" and player_turn != "paper" and player_turn != "scissor":
    print("\nplease enter correct choice!")
    player_turn = input("\nenter your choice rock ,paper,scissor:-")

  possible_way = ["rock", "paper", "scissor"]
  computer_move = random.choice(possible_way)
  print("\n you choose:-", dic[player_turn], "\ncomputer choose:-",
        dic[computer_move], "\n")

  if player_turn == computer_move:
    print("both players selected", dic[player_turn], "\nits a tie")
    tie = tie + 1
  elif player_turn == "rock":
    if computer_move == "scissor":
      print("\n rock smashes the scissor YOU win")
      player_score = player_score + 1
    else:
      print("💻computer win")
  elif player_turn == "paper":
    if computer_move == "rock":
      print(" paper🧻 cover the rock🪨! player win")
      player_score = player_score + 1
    else:
      print("💻computer win")
      computer_score = computer_score + 1

  elif player_turn == "scissor":
    if computer_score == "paper":
      print("scissor✂️ cut the paper🧻", NAME, "win")
      player_score = player_score + 1
    else:
      print("computer win")
      computer_score = computer_score + 1

  play_agin = input("do you want to play agin(yes to enter no to exit ):-")
  if play_agin == "no":
    break

  Flag = True
  while play_agin != "yes":
    Flag = True
    print("\nselect correct option yes/no")
    play_agin = input("do you want to play again(yes\no):-")
    if play_agin == "no":
      Flag = False
      break

  if Flag == False:
    break

print()
print("\n🙏ngame end,thank u for playing🙏")
print("\nscores of both player:-")
print("\n💻computer_score", computer_score)
print("\n", NAME, player_score)
print("\ntotal tie in the game", tie)
print()

if player_score > computer_score:
  print(NAME, "win")
elif player_score == computer_score:
  print("\ngame Tie😒")
else:
  print("\ncomputer win")

