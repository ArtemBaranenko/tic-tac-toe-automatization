def create_board():
    """
    Creates the board.

    Returns:
        list: Board structure
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    """
    Prints out the board.

    Args:
        board (list): Board which will be printed out.
    """
    under_score=0

    for row in board:
        print('|'.join(row))
        under_score+=1
        if under_score <=2:
            print('-' * 5)

def is_win(player, board):
    """
    Checks whether there are specified symbols on the board in the row horizontally, vertically, or diagonally.

    Args:
        player (str): Specified player.
        board (list): Board.

    Returns:
        bool: Either function will return True if the specified player won or False if they did not.
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def main():
    """
    Ties up all the functions together in one sequence.

    Creates the board -> Takes the move -> Checks whether player won or not -> repeats 9 times -> then calls it a draw.
    """
    current_player = 'X'
    results = 0

    # Loop in order to be able to play game multiple times without breaking the count of wins
    while True:
        moves = 0
        board = create_board()

        # 9 iterations in order to stop when it is a draw
        while moves < 9:
            print_board(board)

            #Takes the move
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
            #Adds the move if the cell is empty
            if board[row][col] == ' ':
                board[row][col] = current_player
                win = is_win(current_player,board) #Checks for the win

                #If it is a win -> prints out the message
                if win:
                    results+=1
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    print(f"Number of wins during the game: {results}")

                    # Restarts the game if chosen
                    answer = input("Play again ? y/n: ")
                    if answer.lower() == "n":
                        exit(0)
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'  # Switch player
                    moves += 1
            else:
                print("Cell already occupied! Try again.")
        if moves >= 9:
            print_board(board)
            print("It's a draw!")
            print(f"Number of wins during the game: {results}")

if __name__ == "__main__":
    main()
