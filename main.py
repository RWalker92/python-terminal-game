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

def deal_card():
    global player_score
    card = random.choice(list(cards.keys()))
    player_hand.append(card)
    player_score += cards[card][0]

while player_score < 21:
    print(f"{player_name} you are dealt {player_hand} for a score of {player_score}")
    deal_again = input("Would you like another card? y/n ").lower()
    if deal_again == "y":
        deal_card()
        print(f"You were dealt a {player_hand[-1]}")
        if player_score > 21:
            print("You bust!")
    else:
        print(f"You end with a total score of {player_score}")
        break

print("Lets see what the dealer scores.....")
print(f"The dealer has drawn the cards {dealer_hand} for a score of {dealer_score}")

if player_score > 21:
    print("You bust, dealer wins!")
elif dealer_score > player_score:
    print("Dealer Wins!")
elif player_score > dealer_score:
    print(f"{player_name} Wins!")
else:
    print("No winner!")