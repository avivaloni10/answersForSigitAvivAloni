#Author: aviv aloni

def isWinner(game, num):
    return ((game[0][0] == num and game[0][1] == num and game[0][2] == num) or  # Across the top
            (game[1][0] == num and game[1][1] == num and game[1][2] == num) or  # Across the middle
            (game[2][0] == num and game[2][1] == num and game[2][2] == num) or  # Across the bottom
            (game[0][0] == num and game[1][0] == num and game[2][0] == num) or  # Down the left side
            (game[0][1] == num and game[1][1] == num and game[2][1] == num) or  # Down the middle
            (game[0][2] == num and game[1][2] == num and game[2][2] == num) or  # Down the right side
            (game[0][0] == num and game[1][1] == num and game[2][2] == num) or  # Diagonal
            (game[0][2] == num and game[1][1] == num and game[2][0] == num))  # Diagonal


game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]] # Define gameboard
if isWinner(game, 1):
    print("Player1 won!\n")
elif isWinner(game, 2):
    print("Player2 won!\n")
else:
    print("Draw!\n")