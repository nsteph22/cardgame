# Card Game Final Project – INST126
# Author: Nahjah
# Description:
# This is a two-player card game (player vs. computer). Cards are shuffled and dealt, and players take turns
# playing cards by matching suit. Whoever plays the highest card in the suit wins the round.
# Advanced Features:
# - Uses time.sleep() to slow the game and make it feel more natural
# - Uses time.strftime() to print a timestamp for each round
# Resources:
# - time.sleep(): https://www.youtube.com/watch?v=s3v7iMEzBtY
# - time.strftime(): https://www.youtube.com/watch?v=qk7qqbZxJGo
# - https://www.youtube.com/watch?v=89cGQjB5R4M
# - https://www.youtube.com/watch?v=Bp6L85JWB9k

import random
import time

# Get player name
player = input("Name: ")

# Create the deck (no King)
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
cards = []

value = 1
for rank in ranks:
    for suit in suits:
        cards.append([rank + " of " + suit, value, suit])
    value += 1

random.shuffle(cards)

# Deal 8 cards to each player
player_cards = []
computer_cards = []
for i in range(8):
    player_cards.append(cards.pop())
    computer_cards.append(cards.pop())

player_score = 0
computer_score = 0

# Decide who starts randomly
first = random.choice(["player", "computer"])

# Game Loop
while len(player_cards) > 0 and len(computer_cards) > 0:
    print("\n------------------")
    print(player + "'s cards:")
    for i in range(len(player_cards)):
        print(str(i + 1) + ":", player_cards[i][0])

    if first == "player":
        print("Your turn.")
        try:
            choice = int(input("Card #: "))
            player_card = player_cards.pop(choice - 1)
        except:
            player_card = player_cards.pop(0)

        match_suit = player_card[2]
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] You played:", player_card[0])
        time.sleep(1)

        has_suit = False
        for card in computer_cards:
            if card[2] == match_suit:
                has_suit = True
                break

        if has_suit:
            highest_card = None
            for card in computer_cards:
                if card[2] == match_suit:
                    if highest_card is None or card[1] > highest_card[1]:
                        highest_card = card
            computer_card = highest_card
            computer_cards.remove(computer_card)
        else:
            computer_card = computer_cards.pop(0)

        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Computer played:", computer_card[0])
        time.sleep(1)

    else:
        computer_card = computer_cards.pop(0)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Computer played:", computer_card[0])
        time.sleep(1)

        match_suit = computer_card[2]
        has_suit = False
        valid_cards = []
        for i, card in enumerate(player_cards):
            if card[2] == match_suit:
                has_suit = True
                valid_cards.append(i)

        if has_suit:
            print("You must play a", match_suit, "card.")
            print("Valid options:", " ".join(str(i + 1) for i in valid_cards))
            valid_choice = False
            while not valid_choice:
                try:
                    choice = int(input("Card #: "))
                    if choice - 1 in valid_cards:
                        player_card = player_cards.pop(choice - 1)
                        valid_choice = True
                    else:
                        print("You must follow suit with a", match_suit)
                except:
                    print("Invalid choice. Try again.")
        else:
            print("You don't have any", match_suit, "cards. Play any card.")
            choice = int(input("Card #: "))
            player_card = player_cards.pop(choice - 1)

        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] You played:", player_card[0])
        time.sleep(1)

    # Determine winner
    if player_card[2] == match_suit and computer_card[2] == match_suit:
        if player_card[1] > computer_card[1]:
            print("You win round!")
            player_score += 1
            first = "player"
        else:
            print("Computer wins round!")
            computer_score += 1
            first = "computer"
    elif player_card[2] == match_suit:
        print("You win round!")
        player_score += 1
        first = "player"
    else:
        print("Computer wins round!")
        computer_score += 1
        first = "computer"

    time.sleep(1)

    # Reveal card from deck
    if len(cards) > 0:
        revealed_card = cards.pop()
        print("Revealed card:", revealed_card[0])
        time.sleep(1)

    # Deal 4 more cards when each player has 4 left
    if len(player_cards) == 4 and len(computer_cards) == 4 and len(cards) >= 8:
        print("\nDealing 4 more cards each...")
        for i in range(4):
            player_cards.append(cards.pop())
            computer_cards.append(cards.pop())

    # End early if someone reaches 9 and the other has at least 1
    if (player_score >= 9 and computer_score >= 1) or (computer_score >= 9 and player_score >= 1):
        print("Game ends early - winning score reached!")
        break

    # Check for "shoot the moon"
    if len(player_cards) == 0 and len(computer_cards) == 0:
        if player_score == 16 and computer_score == 0:
            print("You shot the moon!")
            player_score = 17
        elif computer_score == 16 and player_score == 0:
            print("Computer shot the moon!")
            computer_score = 17

# Final score
print("\nGAME OVER")
print("Your score:", player_score)
print("Computer score:", computer_score)

if player_score > computer_score:
    print("YOU WIN!")
else:
    print("COMPUTER WINS!")
