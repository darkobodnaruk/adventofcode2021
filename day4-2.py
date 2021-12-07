#!/usr/local/bin/python3

import re
import sys
lines = open("day4_input.txt").readlines()

drawn_numbers = list(map(lambda n: int(n), lines[0].split(",")))
print(drawn_numbers)

def load_boards(lines):
    boards = []
    board_idx = 0
    for line in lines:
        if line.strip() == "":
            # empty line, start new board
            boards.append([])
            board_idx = len(boards) - 1
        else:
            # load line into board
            boards[board_idx].append(list(map(lambda n: int(n), line.split())))
    return boards

def print_board(board):
    if board is None:
        return
    for row in board:
        print("| " + " ".join([(("%2d" % num) if (num != None) else "  ") for num in row]))

def check_winner(board, drawn_number):
    board_size = len(board[0])
    for idx_row, row in enumerate(board):
        for idx_number, number in enumerate(row):
            if number == drawn_number:
                board[idx_row][idx_number] = None
    # check row
    for idx_row, row in enumerate(board):
        if all([n is None for n in row]):
            print(f"winner board (on row): {board}")
            return board
    # check column
    for idx_col, _ in enumerate(board[0]):
        col = [row[idx_col] for row in board]
        if all([n is None for n in col]):
            print(f"winner board (on col): {board}")
            return board
    return False

def calculate_score(board, number):
    unmarked_numbers_sum = 0
    for row in board:
        for num in row:
            if num != None:
                unmarked_numbers_sum += num
    print(f"unmarked_numbers_sum: {unmarked_numbers_sum}")
    return unmarked_numbers_sum * number


boards = load_boards(lines[1:])

for number in drawn_numbers:
    print(f">>> drawn_number: {number}")
    idx_boards_to_delete = []
    if all([board is None for board in boards]):
        break
    for idx, board in enumerate(boards):
        if idx == 56 or idx == 74:
            print(f"board idx {idx}")
            print_board(board)
        if board == None:
            continue
        winner = check_winner(board, number)
        if winner:
            score = calculate_score(board, number)
            print(f"score: {score}")
            idx_boards_to_delete.append(idx)
    if len(idx_boards_to_delete) > 1:
        print("wat??")
    for idx in idx_boards_to_delete:
        print(f"removing board {idx}")
        print("")
        boards[idx] = None
