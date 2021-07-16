print("Welcome to Treasure Island in the middle of the deep blue sea!\n")
print('''
 _                                     _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 
''')

choice_1 = input('Where do you choose to go? Enter "left" or "right" ').lower()

if choice_1 == "left":
    choice_2 = input('Enter "wait" to wait for the boat or "swim" to swim across ' ).lower()
    if choice_2 == "wait":
        choice_3 = input("Great! You've made it to the house in the middle of the island; There are three doors - Which color do you choose? Red, Yellow or Green? ").lower()
        if choice_3 == "yellow":
            print("Congrats!! You found the treasure!")
        else:
            print("Sorry! You unlocked a room leading to an abyss! Game Over.")
    else:
        print("Sorry, you were eaten by the fat trout! Game over")
else: 
    print("Game Over! You fell into an abyss")
