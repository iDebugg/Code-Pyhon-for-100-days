import random

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

the_game = random.randint(0, 2)
print(the_game)

player_input = int(input("What do you choose? 0 for rock, 1 for paper or 2 for scissors. \n"))
if the_game == 0 & player_input == 1 :
    print("You win!")
elif the_game == 0 and player_input == 2 :
    print("You lose!")
elif the_game == 0 and player_input == 0 :
    print("A draw!")
elif the_game == 1 and player_input == 0 :
    print("You lose!")
elif the_game == 1 and player_input == 2 :
    print("You win!")
elif the_game == 1 and player_input == 1:
    print("A draw!")
elif the_game == 2 and player_input == 0 :
    print("You win!")
elif the_game == 2 and player_input == 1 :
    print("You lose!")
elif the_game == 2 and player_input == 2 :
    print("A draw!")
else:
    print("Wrong input")

