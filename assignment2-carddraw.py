# CARD DRAW
# Author: Mariane McGrath

# Deck of Cards API    https://deckofcardsapi.com/ -- This API simulates dealing a deck of cards

# Write a program that "deals" (prints out) 5 cards:

# Step 1: Shuffle the deck and get the deck_id
# Step 2: Draw 5 cards, one by one, and print the value and the suit of each card.
# BONUS POINTS: Get two hands and see which one is better

# Import the requests library to make HTTP requests to the Deck of Cards API
import requests

# Step 1: Shuffle the deck and get the deck_id
response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
data = response.json()
deck_id = data['deck_id']