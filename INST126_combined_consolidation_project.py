import random

# get player name
player = input("Name: ")

# make cards with no king
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
cards = []
# make deck
value = 1
for rank in ranks:
    for suit in suits:
        # Add each card just once
        cards.append([rank + " of " + suit, value, suit])
    value = value + 1  # Increment value for each rank
# mix the cards
random.shuffle(cards)

# deal the cards
player_cards = []
computer_cards = []
for i in range(8):  # Deal 8 cards each
    player_cards.append(cards.pop())
    computer_cards.append(cards.pop())

# keep track of score
player_score = 0
computer_score = 0

# who starts is random
first = random.choice(["player", "computer"])

# game Loop
while len(player_cards) > 0 and len(computer_cards) > 0:
    print("\n------------------")
    print(player + "'s cards:")
    for i in range(len(player_cards)):
        print(str(i + 1) + ":", player_cards[i][0])
    
    # player turn
    if first == "player":
        print("Your turn.")
        try:
            choice = int(input("Card #: "))
            player_card = player_cards.pop(choice - 1)
        except:
            # If error, just take first card
            player_card = player_cards.pop(0)
        
        match_suit = player_card[2]
        print("You played:", player_card[0])
        
        # Computer must follow suit if possible
        has_suit = False
        for card in computer_cards:
            if card[2] == match_suit:
                has_suit = True
                break
        
        if has_suit:
            # Computer follows suit
            highest_card = None
            for card in computer_cards:
                if card[2] == match_suit:
                    if highest_card is None or card[1] > highest_card[1]:
                        highest_card = card
            computer_card = highest_card
            computer_cards.remove(computer_card)
        else:
            # Computer plays any card
            computer_card = computer_cards.pop(0)
            
        print("Computer played:", computer_card[0])
        
    # computer turn    
    else:
        computer_card = computer_cards.pop(0)
        print("Computer played:", computer_card[0])
        match_suit = computer_card[2]
        
        # Check if player has the suit
        has_suit = False
        valid_cards = []
        for i, card in enumerate(player_cards):
            if card[2] == match_suit:
                has_suit = True
                valid_cards.append(i)
        
        if has_suit:
            print("You must play a", match_suit, "card.")
            print("Valid options:", end=" ")
            for i in valid_cards:
                print(str(i + 1), end=" ")
            print()
            
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
    
    print("You played:", player_card[0])
    print("Computer played:", computer_card[0])
    
    # determine  the winner
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
    
    # show a card from the deck
    if len(cards) > 0:
        revealed_card = cards.pop()
        print("Revealed card:", revealed_card[0])
    
    # Deal more cards when both are down to 4
    if len(player_cards) == 4 and len(computer_cards) == 4 and len(cards) >= 8:
        print("\nDealing 4 more cards each...")
        for i in range(4):
            player_cards.append(cards.pop())
            computer_cards.append(cards.pop())
    
    # end the game early iff one player reaches 9 points and other has at least 1
    if (player_score >= 9 and computer_score >= 1) or (computer_score >= 9 and player_score >= 1):
        print("Game ends early - winning score reached!")
        break
        
    # check for shooting the moon
    if len(player_cards) == 0 and len(computer_cards) == 0:
        if player_score == 16 and computer_score == 0:
            print("Computer shot the moon!")
            computer_score = 17
        elif computer_score == 16 and player_score == 0:
            print("You shot the moon!")
            player_score = 17

# Show final score
print("\nGAME OVER")
print("Your score:", player_score)
print("Computer score:", computer_score)

if player_score > computer_score:
    print("YOU WIN!")
else:
    print("COMPUTER WINS!")