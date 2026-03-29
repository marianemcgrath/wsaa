# CARD DRAW
# Author: Mariane McGrath

# Deck of Cards API    https://deckofcardsapi.com/ -- This API simulates dealing a deck of cards

# Write a program that "deals" (prints out) 5 cards:
# Step 1: Shuffle the deck and get the deck_id
# Step 2: Draw 5 cards, one by one, and print the value and the suit of each card.
# BONUS POINTS: Get two hands and see which one is better

#########################              ##################################

# Import the requests library to make HTTP requests to the Deck of Cards API

import requests

# Step 1: Shuffle the deck and get the deck_id

response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
deck_id = response.json()['deck_id']

# Step 2: Draw two hands of 5 cards each and print the value and suit of each card

response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=10")
cards = response.json()['cards']

hand1 = cards[:5]
hand2 = cards[5:]

# Calculating the score of a hand, based on the cards received from the API.

# The scoring system is:
# - Straight Flush: 6 points
# - Four of a Kind: 5 points
# - Full House: 4 points
# - Flush: 3 points
# - Straight: 2 points
# - Three of a Kind: 1 point
# - Two Pair: 0 points
# - High Card: -1 point

def calculate_score(hand):
    values = [card['value'] for card in hand]
    suits = [card['suit'] for card in hand]

    if is_straight_flush(hand):
        return 6
    elif is_four_of_a_kind(hand):
        return 5
    elif is_full_house(hand):
        return 4
    elif is_flush(hand):
        return 3
    elif is_straight(hand):
        return 2
    elif is_three_of_a_kind(hand):
        return 1
    elif is_two_pair(hand):
        return 0
    else:
        return -1

# Source: https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python/

# Print the cards in each hand and their scores to determine which hand is better

# Print the cards in hand 1
print("Hand 1:")
for cards in hand1:
    print(f"{cards['value']} of {cards['suit']}")
score1 = calculate_score(hand1)
print(f"Score: {score1}")

# Print the cards in hand 2
print("\nHand 2:")
for cards in hand2:
    print(f"{cards['value']} of {cards['suit']}")
score2 = calculate_score(hand2)
print(f"Score: {score2}")

# Determine which hand is better based on the scores (ranks)

print(f"\nHand 1 score: {score1}")
print(f"Hand 2 score: {score2}")

if score1 > score2:
    print("\nHand 1 wins!")
elif score2 > score1:
    print("\nHand 2 wins!")
else:
    print("\nIt's a tie!")