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
        
