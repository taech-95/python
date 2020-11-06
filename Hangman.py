import random
#picking random word and checking answer
word_list=["ukraine", "poland", "usa","germany","france","football", "destiny"]
chosen_word = random.choice(word_list)

print (chosen_word)
output =""
for i in chosen_word:
    output+="_ "

# print(output)
# print(type(output))
guess = input("Chose a letter: \n").lower()
# print(guess)
indexer =0
for i in chosen_word:
    if chosen_word[indexer] == guess:
        print ("true")
# print(output)