# Display art
from art import logo,vs

# function to format the data dictionary, # Format the account data into printable format
def format_data(account):
    """Take the account data and retruns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name} a {account_desc} from {account_country}")

# fucntion which check the answer 
def check_answer(user_guess, a_follower, b_follower):
    """Take a user's guess and the follower counts and returns if they got it right. """
    if a_follower > b_follower:
        return guess == "a" # return true if guess = a
    else :
        return guess == "b" # reurn false if guess = b

print(logo)
#score count
score = 0


# Generate a random account from the game data 
import random
from game_data import data
account_B = random.choice(data)

flag = True

while flag:

    # Overwriting the accout A with B and regenerate account_B 
    account_A = account_B
    account_B = random.choice(data)

    if account_A == account_B:
        account_B = random.choice(data)



    print(f"Compare A: {format_data(account_A)} ")
    print(vs)
    print(f"Compare B: {format_data(account_B)}")

    # Ask user for a guess 
    guess = input("Who has more followers? Type A or B: ").lower()

    #Clear the screen
    print("\n"*20)
    print(logo)

    # Check if user is correct 
    ## Get follower count of each account 
    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]

    is_correct = check_answer(guess, a_follower_count,b_follower_count)
    ## use if statemnet to check if user is correct 


    # Give user feedback on theri guess 
    if is_correct:
        score += 1
        print(f"You are right! Current score {score}")

    else:
        print(f"Sorry, that's wrong. Final Score {score}")
        flag = False

# Score keeping 


# Make the game repeatable 

# Making account at position B become the next account at position A    

