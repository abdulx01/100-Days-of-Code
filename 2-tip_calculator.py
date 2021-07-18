print("Welcome to the tip calculator!\n")
# Read in the bill amount, percentage tip, num_people to share
bill_amt = float(input("What's the bill amount? $"))
perc_tip = int(input("What percentage would you like to pay as tip?"))/100
num_share = int(input("How many people are sharing the bill?"))

each_person_pays = (bill_amt * (1 + perc_tip))/num_share
amt_rounded = round(each_person_pays,2)
amt_formatted = "{:.2f}".format(amt_rounded)

print(f"Okay, each person should pay ${amt_formatted}")
