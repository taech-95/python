import art

bids_dictionary={}
flag=True

print(art.logo)
print("Welcome to the Secret Auction")

def who_win_auction(bid):
    max_bid=0
    bid_amount=0
    winner=""
    for bidder in bid:
        bid_amount = int(bid[bidder])
        if bid_amount>max_bid:
            max_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid {max_bid}")


while flag==True:
    name = input("What is your name?\n")
    bid = input ("What is your bid?\n")
    bids_dictionary[name]=bid
    one_more_time = input("If you want to add one more person, type 'yes', else 'no' \n").lower()
    if one_more_time =="no":
        flag=False
        who_win_auction(bids_dictionary)
   