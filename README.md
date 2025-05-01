# Python Terminal Blackjack Game

## Description

A command-line implementation of the classic casino card game Blackjack (also known as 21). Players compete against a computer dealer, trying to get cards that total as close to 21 as possible without going over.

## Features

- Player vs Dealer gameplay
- Modified Blackjack rules implementation
- Option to Hit or Stand
- Score tracking

## Installation

```bash
git clone https://github.com/RWalker92/python-terminal-game
cd python-terminal-game
python main.py

```

## Requirements

Python 3.6 or higher

## How to Play

1. Run the game using the command above
2. You will be dealt two cards
3. Choose to 'hit' (take another card) or 'stand' (keep current cards)
4. Try to get closer to 21 than the dealer without going over

## Game Rules

- Ace only counts as 1 (might implement it being 1 OR 11 in future)
- Face cards (Jack, Queen, King) count as 10
- Numbered cards count as their face value
- Going over 21 results in a "bust" and automatic loss
- Dealer draws 2 cards and that is it, these aren’t revealed until after the player sticks or busts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Ryan Walker
