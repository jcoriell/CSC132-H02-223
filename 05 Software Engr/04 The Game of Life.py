import os
import sys
import copy
from time import sleep


def count_neighbors(board, row, col):
    neighbors = 0

    for i in range(-1, 2):  # really -1 to 1
        for j in range(-1, 2):  # really -1 to 1
            if i == 0 and j == 0:
                continue
            if board[row+i][col+j] == "*":
                neighbors += 1

    return neighbors

def compute_next_board(board):
    board_size = len(board)
    next_board = copy.deepcopy(board)

    for row in range(1, board_size-1):
        for col in range(1, board_size - 1):
            neighbors = count_neighbors(board, row, col)

            lonely = neighbors < 2
            overcrowded = neighbors > 3
            perfect_fit = neighbors == 2 or neighbors == 3

            alive = board[row][col] == "*"
            available = board[row][col] != "*"

            if alive and (lonely or overcrowded):
                next_board[row][col] = " "
            
            if available and perfect_fit:
                next_board[row][col] = "*"
    
    return next_board


def print_board(board):
    """Prints the board in a prettier format."""
    board_size = len(board)
    # game board header
    print(" ", end=" ")
    for col_number in range(1, board_size-1):
        print(col_number, end=" ")
    print()

    # print each row
    for row_num, row in enumerate(board):

        if row_num == 0 or row_num == board_size-1:
            continue

        print(row_num, end=" ")

        for col_num, item in enumerate(row):
            if col_num == 0 or col_num == board_size - 1:
                continue
            print(item, end=" ")
            
        print()

# Main Portion

GENERATIONS = 30

board = []

for line in sys.stdin:

    content = []
    for character in line:
        if character == "\n":
            continue

        content.append(character)
    
    board.append(content)

os.system("clear")
print_board(board)
for gen in range(GENERATIONS):
    sleep(0.5)
    os.system("clear")
    board = compute_next_board(board)
    print_board(board)