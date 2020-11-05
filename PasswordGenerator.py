import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters=int(input("How many letters do you want in your password\n"))
nr_numbers=int(input("How many numbers do you want in your password\n"))
nr_symbols=int(input("How many symbols do you want in your password\n"))

# randomLetters = random.choice(letters)
# randomNumbers=random.choice(numbers)
# randomSymbols=random.choice(symbols)
# print(nr_letters)
# print(type(nr_letters))
passwordTemplate=[]
# counter=0
for i in range(nr_letters):
    passwordTemplate+=random.choice(letters)

for i in range(nr_numbers):
    passwordTemplate+=random.choice(numbers)

for i in range(nr_symbols):
    passwordTemplate+=random.choice(symbols)

    # passwordTemplate=passwordTemplate+randomLetters
    # print(passwordTemplate)
    # counter+=1
    # if(counter==int(nr_letters)):
    #     break

# print(passwordTemplate)
random.shuffle(passwordTemplate)
password=""
# print(passwordTemplate)
for i in passwordTemplate:
    password+=i
print(f"Your password is {password}")