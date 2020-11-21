import random

#picking random word and checking answer
lives = 6
from hangman_art import logo, stages
from hangman_words import word_list
print(logo)

chosen_word = random.choice(word_list)
# print (chosen_word)
#preparing output
output=[]
indexer=0
for i in chosen_word:
    output+="_"
print(output)
flag ="_"
gameOver = False
while gameOver == False:
    guess = input("Chose a letter: ").lower()
    
    if guess in output:
      print(f"You already pick this letter {guess}")
    
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            output[i] = guess 
   
   
    if guess not in chosen_word:
        print(f"You guessed {guess} is not in chosen word. You lose a life ")
        lives-=1 
        print(stages[lives]) 
          
    #print(lives)
    print(output)
    #check lives
    if lives <=0:
        print("You lose")
        gameOver = True
    #check for blankes 
    if flag not in output:
        print("You win! Good Job! :)")
        gameOver = True
print (f"Chosen word was {chosen_word}")
print("Game Over")