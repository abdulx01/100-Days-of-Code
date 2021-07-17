import random

print("Welcome to the game! \n")
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

game_choice = [rock,paper,scissors]

# Read in the user's choice
user_choice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors \n"))
comp_choice = random.randint(0,2)

if user_choice not in [0,1,2]:
    print("Invalid choice; you lost the game")
else:
    print("You chose: \n")
    print(game_choice[user_choice])
    print("Computer chose: \n")
    print(game_choice[comp_choice])
    
    if user_choice ==  comp_choice:
        print("It's a draw")
    elif user_choice == 2 and comp_choice == 0:
        print("Sorry, You lost!")
    elif user_choice > comp_choice:
        print("Congrats! You won!")
    elif user_choice == 0 and comp_choice == 2:
        print("Congrats! You won!")
    elif user_choice < comp_choice:
        print("Sorry, You lost!")
