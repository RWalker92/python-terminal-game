import random
cards = {"A": [1], "2": [2], "3": [3], "4": [4], "5": [5], "6": [6], "7": [7], "8": [8], "9": [9], "10": [10], "J": [10], "Q": [10], "K": [10]}

player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0

player_name = input("Enter your name: ")
print(f"Welcome to Blackjack, {player_name}!")
print("The goal of the game is to get as close to 21 as possible without going over.")
print("You will be playing against the dealer. Let's start!")
print("Dealing cards...")

# Deal two cards to the player and one card to the dealer

for _ in range(2):
    card = random.choice(list(cards.keys()))
    player_hand.append(card)
    player_score += cards[card][0]

    card = random.choice(list(cards.keys()))
    dealer_hand.append(card)
    dealer_score += cards[card][0]

