import random

def deal_card():
  # cards - ACE (11), number cards (face value) and face cards (10 pts each) 
  cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

# define lists to hold cards drawn
user_cards = []
comp_cards = []

# draw 2 cards at random initially
for _ in range(2):
  user_cards.append(deal_card())
  comp_cards.append(deal_card())
  

  



