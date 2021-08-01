from random import randint

EASY_TURNS = 5
HARD_TURNS = 10

def check_answer(guess,answer,turns):
  """ Checks the user's guess against the answer. Returns the number of attempts remaining"""
  if guess < answer:
    print("Too low")
    return turns-1
  elif guess > answer:
    print("Too high")
    return turns-1
  else:
    print(f"You got it! The number was {answer}")


def set_difficulty():
  level = input("Choose difficulty: Type 'hard' or 'easy'")
  if level == 'easy':
    return EASY_TURNS
  else:
    return HARD_TURNS
        
def num_guessing_game():
  
  # Choose a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
 
  turns = set_difficulty()
  # Repeat the guessing functionality if they get it wrong and still have attempts less
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    
    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

num_guessing_game()
