# Tic-Tac-Toe Game

This is a simple command-line Tic-Tac-Toe game written in Python.

Updated 08/04/2026.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Documentation](#documentation)

## Overview

This program allows two players to play Tic-Tac-Toe in the console.  
Players take turns entering their moves, and the board updates after each turn.

The game checks for:

- win conditions (rows, columns, diagonals)
- draw (when all cells are filled)

After a win, players can choose to restart the game.  
The total number of wins is tracked during the session.

## Usage

Run the game using Python:

```bash
python tic_tac_toe.py
```

Follow the prompts to enter row and column numbers to make your moves.

## Documentation

| Method                  | Description                             |
|-------------------------|-----------------------------------------|
| `create_board()`        | Creates an empty 3x3 board              |
| `print_board(board)`    | Displays the board in the console       |
| `is_win(player, board)` | Checks if the player has won            |
| `main()`                | Controls the game loop and player turns |

