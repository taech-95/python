import random
from art import logo,vs
from dictionary import data


# # first chose

def formating(data1):
    account_name1 = data1["name"]
    acount_description1 = data1["description"]
    account_country1 = data1["country"]
    return (f" {account_name1}, a {acount_description1}, from {account_country1}")

def game_print():
    print (f"Compare A: {formating(compare_a)}")
    print("vs")
    print (f"Against B: {formating(compare_b)}")


#random data from dictionary + removing from data set
def chose_the_next_one(data):
    compare_next = random.choice(data)
    data.remove(compare_next)
    return compare_next
    
def check(user_choise, a_followers, b_followers):
    
    if user_choise=="a" and a_followers> b_followers :
        return True
    elif user_choise=="b" and a_followers<b_followers:
        return True
    else:
        return False


score=0
next_turn = True
compare_b=chose_the_next_one(data)
    # return score 
while  next_turn: 
    print(logo)
    compare_a=compare_b
    compare_b = chose_the_next_one(data)
    game_print()
    user_choise = input("Who has more followers? Type A or B: ").lower()
    a_followers = compare_a["follower_count"]
    b_followers = compare_b["follower_count"]
    is_correct = check(user_choise,a_followers,b_followers)
    if(is_correct==True):
        score+=1
        print (f"You are right! Current score = {score}.")
    else:
        print(f"Sorry that's wrong. Your score = {score}.")
        next_turn = False


