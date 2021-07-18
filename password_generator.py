import random
print("PyPassword Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Read specifications from the user
num_letters = int(input("How many letters do you want in your password? \n"))
num_numbers = int(input("How many numbers do you want in your password? \n"))
num_symbols = int(input("How many symbols do you want in your password? \n"))

pw_list = []

for char in range(num_letters + 1):
    pw_list.append(random.choice(letters))

for char in range(num_numbers + 1):
    pw_list.append(random.choice(numbers))

for char in range(num_symbols + 1):
    pw_list.append(random.choice(symbols))
    
random.shuffle(pw_list)

password = ""

for char in pw_list:
    password += char

print(f"Your password is {password}")
