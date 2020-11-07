import random
#picking random word and checking answer
word_list=["ukraine", "poland", "usa","modern","soccer","shakhtar","germany","france","football", "destiny"]
chosen_word = random.choice(word_list)
print (chosen_word)
#preparing output
output=[]
indexer=0
for i in chosen_word:
    output+="_"

print(output)
# print(type(output))
# user letter
guess = input("Chose a letter: \n").lower()
print(guess)
indexer =0
#testing if chosen word contain user letter
for i in chosen_word:
    if chosen_word[indexer] == guess:
        print ("Right") 
        output[indexer] = guess 
    else:
        print("Wrong")
    indexer+=1
print(output)