import random
from art import logo,vs
from dictionary import data





# for name, follower_count, description, country in data:

# first chose
def choosing_data(data):
    chose_the_next_one(data)
    print(vs)
    chose_the_next_one(data)
    return data

#random data from dictionary + removing from data set
def chose_the_next_one(data):
    compare_next = random.choice(data)
    data.remove(compare_next)
    print(compare_next)
    
print(logo)
data = choosing_data(data)
