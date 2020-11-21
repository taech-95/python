from art import logo
import random 


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_card():
    #chosing a random card
    random_card = random.choice(cards)
    return random_card

#score calculation
def results(scores):
    result =0
    result =sum(scores)
    if(11 in scores and result>21):
            #ace score check 
        scores.remove(11)
        scores.append(1)
        result = 0
        result = sum(scores)
    else:
        return result
    return result


print(logo)
start_game_one_more_time=True
while start_game_one_more_time:
    user_choise_flag = True
    dealer_score = []
    user_score = []
    start_game= input("Do you want to play Black Jack. Type 'y' or 'n': \n").lower()
    if start_game =="y":
        for i in range(0,2,1):
            user_score.append(random_card())
            dealer_score.append(random_card())
    else:
        start_game_one_more_time = False
    
    user_result = results(user_score)   
    dealer_result = results(dealer_score)  
    print(f"Your cards: {user_score}, current score: {user_result}")
    print(f"Computer first card: {dealer_score[0]}")
    if(dealer_result <17):
        dealer_score.append(random_card())
        dealer_result = results(dealer_score)  
        print(dealer_score)
    while user_choise_flag:
        user_choise = input("Type 'y' to get another card, type 'n' to pass: \n").lower()
        if user_choise =="y":
            user_score.append(random_card())
            user_result = results(user_score)   
            
            print(f"Your cards: {user_score}, current score: {user_result}")
            print(f"Computer first card: {dealer_score[0]}")
        else:
            print(f"Your final hand {user_score}, current score: {user_result}")
            print(f"Computer final hand {dealer_score}, current score: {dealer_result}")
            user_choise_flag = False
          
 
    if( user_result == dealer_result):
        print("Draw")
    elif (user_result>21):
        print("You went over. You lose")
    elif (dealer_result >21):
        print("Dealer went over. You Win")
    elif (user_result==21 or dealer_result==21):
        if(user_result==21):
            print("Black Jack! Wow you win")
        else:
            print("Dealer wins :( He has black Jack")
    elif (user_result>dealer_result):
        print("Great Job, You win")
    else:
        print ("Dealer wins, you lose :(")
    
   
