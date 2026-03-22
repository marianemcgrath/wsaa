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
import random, time
from random import shuffle
from enum import Enum

# Step 1: Shuffle the deck and get the deck_id

response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
deck_id = response.json()['deck_id']

# Step 2: Draw two hands of 5 cards each and print the value and suit of each card

response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=10")
cards = response.json()['cards']

hand1 = cards[:5]
hand2 = cards[5:]

# Calculating the score of a hand, based on the cards received from the API. 
# Face cards (Jack, Queen, King) are worth 10 points, Aces are worth 11 points, and all other cards are worth their each value

# Calculating the score of a hand based on the cards and suits
def calculate_score(hand):
    score = 0
    for card in hand:
        value = card['value']
        suit = card['suit']
        if value in ['JACK', 'QUEEN', 'KING']:
            score += 10
        elif value == 'ACE':
            score += 11
        else:
            score += int(value)   