# write pseudo code or make flow chart of the logic which make easier to do coding 
# that is why we study ER/ERD diagrams 

from logo import logo
import os
print(logo)

bidding_finised = False #make the variable sensable 

bid = {}

def highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    #{name:bids,name2:bid}
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder] # getting value by key 
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# use while loop to take input from users until the flag value change  
while not bidding_finised: #use not to flip the value
    name = input("What is your name?")
    price = int(input("What is your bid? $"))
    bid[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")

    if should_continue == 'no':
        bidding_finised = True
        highest_bidder(bid)
    elif should_continue == 'yes':
        # clearing the screen 
        os.system('cls')


# you can use pythontutor or any other website (thonny pyhton ide) to visualize your code





