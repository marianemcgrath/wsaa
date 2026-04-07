# CARD DRAW
# Author: Mariane McGrath

# Deck of Cards API    https://deckofcardsapi.com/ -- This API simulates dealing a deck of cards

# This program "deals" (prints out) 5 cards:
# Step 1: Shuffle the deck and get the deck_id
# Step 2: Draw 5 cards, one by one, and print the value and the suit of each card.
# BONUS POINTS: Get two hands and see which one is better


# Import library to make HTTP requests
try:
    import requests
except ImportError:
    print("Error: requests library is not installed. Install it using: pip install requests")
    exit()


# Step 1: Shuffle the deck and get the deck_id
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
deck_id = response.json()['deck_id']


# Step 2: Draw two hands of 5 cards each and print the value and suit of each card
response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=10")
cards = response.json()['cards']

# Source: https://www.geeksforgeeks.org/python/response-json-python-requests/


hand1 = cards[:5]
hand2 = cards[5:]


# The scoring system is:
# - Straight Flush: 8 points
# - Four of a Kind: 7 points
# - Full House: 6 points
# - Flush: 5 points
# - Straight: 4 points
# - Three of a Kind: 3 points
# - Two Pair: 2 points
# - One Pair: 1 point
# - High Card: 0 points

# When two hands share the same score, the winner is decided by comparing
# card values one by one (highest frequency group first, then by card value).

# Define functions to check for each hand type
def card_value_to_number(value):
    if value == 'ACE':
        return 14
    elif value == 'KING':
        return 13
    elif value == 'QUEEN':
        return 12
    elif value == 'JACK':
        return 11
    else:
        return int(value)

def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)
 
def is_four_of_a_kind(hand):
    values = [card['value'] for card in hand]
    return any(values.count(v) == 4 for v in values)
 
def is_full_house(hand):
    values = [card['value'] for card in hand]
    return any(values.count(v) == 3 for v in values) and any(values.count(v) == 2 for v in values)
 
def is_flush(hand):
    suits = [card['suit'] for card in hand]
    return len(set(suits)) == 1
 
def is_straight(hand):
    values = sorted([card_value_to_number(card['value']) for card in hand])
    return values == list(range(values[0], values[0] + 5))
 
def is_three_of_a_kind(hand):
    values = [card['value'] for card in hand]
    return any(values.count(v) == 3 for v in values) and not is_full_house(hand)
 
def is_two_pair(hand):
    values = [card['value'] for card in hand]
    pairs = sum(1 for v in set(values) if values.count(v) == 2)
    return pairs == 2
 
def is_one_pair(hand):
    values = [card['value'] for card in hand]
    pairs = sum(1 for v in set(values) if values.count(v) == 2)
    return pairs == 1

def rank_values(hand):
    freq = {}
    for card in hand:
        n = card_value_to_number(card['value'])
        freq[n] = freq.get(n, 0) + 1
    groups = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
    return [val for val, cnt in groups for _ in range(cnt)]
 
# Source: https://docs.python.org/3/library/functions.html (any, sorted and set functions)


def calculate_score(hand):
    if is_straight_flush(hand):
        return 8
    elif is_four_of_a_kind(hand):
        return 7
    elif is_full_house(hand):
        return 6
    elif is_flush(hand):
        return 5
    elif is_straight(hand):
        return 4
    elif is_three_of_a_kind(hand):
        return 3
    elif is_two_pair(hand):
        return 2
    elif is_one_pair(hand):
        return 1
    else:
        return 0

def score_label(score):
    labels = {
        8: 'Straight flush',
        7: 'Four of a kind',
        6: 'Full house',
        5: 'Flush',
        4: 'Straight',
        3: 'Three of a kind',
        2: 'Two pair',
        1: 'One pair',
        0: 'High card',
    }
    return labels[score]

# Source: https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python/
# Also used CoPilot (Claude) to simplify the code above, as the code had an error for tiebreakers.

# Print the cards in each hand and their scores to determine which hand is better

# Print the cards in hand 1
print("Hand 1:")
for cards in hand1:
    print(f"{cards['value']} of {cards['suit']}")
score1 = calculate_score(hand1)
print(f"Score: {score1} ({score_label(score1)})")

# Print the cards in hand 2
print("\nHand 2:")
for cards in hand2:
    print(f"{cards['value']} of {cards['suit']}")
score2 = calculate_score(hand2)
print(f"Score: {score2} ({score_label(score2)})")

# Determine which hand is better based on the scores (ranks)
print(f"\nHand 1 score: {score1} ({score_label(score1)})")
print(f"Hand 2 score: {score2} ({score_label(score2)})")

if score1 != score2:
    if score1 > score2:
        print("\nHand 1 wins!")
    else:
        print("\nHand 2 wins!")
else:
    print("\nIt's a tie!")