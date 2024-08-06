import art
# print(art.logo)
import random



user_card = []
computer_card = []

def deal_card():
    """Return a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

for i in range(2):
    user_card.append(deal_card())
    

print(user_card)







