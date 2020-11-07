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
flag ="_"
gameOver = False
while gameOver == False:
    guess = input("Chose a letter: \n").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            output[i] = guess 
    # else:
    #    #print("Wrong")
    if flag not in output:
        print("You win")
        gameOver = True
    print(output)
print("Game Over")