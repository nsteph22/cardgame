# Card Game - INST126 Final Project

## Overview
This is a two-player card game where a human player competes against the computer. Players take turns playing cards by matching suits, and whoever plays the highest card in the matching suit wins the round. The game continues until all cards are played or an early win condition is met.

## How to Use

1. Download or clone the repository to your local machine.
2. Ensure you have Python installed on your computer (Python 3.x or higher).
3. Open a terminal (or Anaconda PowerShell) and navigate to the folder where the script is located.
4. Run the script by typing the following command:

   ```bash
   python card_game.py
   ```

5. The game will prompt you for your name, then deal cards and start the game. Follow the prompts to play against the computer.

## Game Rules
- The deck contains all standard cards except Kings (Ace through Queen in all four suits)
- Each player starts with 8 cards
- Starting player is chosen randomly
- Players must follow suit when possible (play a card of the same suit as the lead card)
- If a player cannot follow suit, they can play any card
- The player who plays the highest card in the matching suit wins the round
- Winner of each round leads the next round
- When players have 4 cards left, 4 more cards are dealt to each player
- Game ends when all cards are played or when one player reaches 9 points and the other has at least 1 point
- Special "shoot the moon" scoring: if a player wins all 16 tricks, they get 17 points

## Features

- Interactive card selection with input validation
- Smart computer AI that follows suit when possible and plays strategically
- Real-time scoring system
- Timestamp logging for each card play
- Error handling for invalid user inputs
- Natural game pacing with timed delays
- Early game termination conditions
- Special "shoot the moon" scoring bonus

## Advanced Features
This project incorporates two advanced topics from the course requirements:

### 1. Random Module (5 points)
- **`random.shuffle()`**: Shuffles the deck at the start of each game to ensure random card distribution
- **`random.choice()`**: Randomly determines which player goes first at the beginning of the game
- These functions are essential to the game's fairness and replayability

### 2. Time Module (5 points)
- **`time.sleep()`**: Adds realistic pacing to the game by pausing between actions (card plays, round results, etc.), making the game feel more natural and easier to follow
- **`time.strftime()`**: Adds timestamps to each card play, showing the exact time when each card was played in format "YYYY-MM-DD HH:MM:SS"
- These timing features significantly enhance the user experience and game flow

## Requirements

- Python 3.x or higher

## Author
Nahjah

## Course
INST126 - Introduction to Programming for Information Science

## License

MIT License   