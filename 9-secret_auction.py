# originally tried in repl.it
from replit import clear

# create an empty dictionary
bid = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amt = bidding_record[bidder]
        if bid_amt > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while not bidding_finished:
  name = input("What is your name? ")
  price = int(input("What is your bid amount? $"))
  bid[name] = price
  should_continue = input("Are there any more bidders? Type 'yes' or 'no'")
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bidder(bid)
  elif should_continue == 'yes':
    clear()
    
  
  
