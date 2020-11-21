import random
from art import logo


print (logo)
def select_difficulty():
    
    print("Welcome to the number guessing game!!!\nI'm thinking of a number between 1 and 100")
    user_choise = input("Choose a difficulty. Type 'easy' or 'hard'   ").lower()
    if user_choise =="hard":
        lives = 5
    else:
        lives =10
    return lives


def make_a_guess(player_lives):
    guessed_number= random.randint(1,100)
    # print(guessed_number)
    while player_lives>0:
        print(f"You have {player_lives} attemps remaining to guess the number")
        number = int(input("Make a guess:   "))
        if guessed_number < number:
            print ("Too high :( \nGuess again.")
            player_lives -=1
        elif guessed_number > number:
            print ("Too low :( \nGuess again.")
            player_lives -=1
        elif guessed_number==number:
            print (f"You guessed !!! Good job, the guessed number was {guessed_number}")
            return
        if(player_lives==0):
            print(f"You lose :( the guessed number was {guessed_number}. You was too close")
            return
       
    #return player_lives


user_choise = True
while user_choise:
    lives = select_difficulty()
    # print (lives)
    make_a_guess(lives)
    one_more_time = input("Do you want to play one more time??? Type 'y' or 'no': " ).lower()
    if one_more_time =="no":
        user_choise = False














