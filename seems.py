# Tic-Tac-Toe Game with Minimax AI

import math
import random

# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    for i in range(3):
        print(f"{board[3*i]} | {board[3*i+1]} | {board[3*i+2]}")
        if i < 2:
            print("---------")

# Check if the board is full
def is_board_full(board):
    return ' ' not in board

# Check for a win condition
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Get available moves
def available_moves(board):
    return [i for i, x in enumerate(board) if x == ' ']

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Get the best move for the AI
def best_move(board):
    move = -1
    best_value = -math.inf
    for i in available_moves(board):
        board[i] = 'X'
        move_value = minimax(board, 0, -math.inf, math.inf, False)
        board[i] = ' '
        if move_value > best_value:
            best_value = move_value
            move = i
    return move

# Main game loop
def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe! You are 'O' and the AI is 'X'.")
    
    while True:
        print_board(board)
        
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] == ' ':
            board[move] = 'O'
        else:
            print("Invalid move, try again.")
            continue

        if check_winner(board, 'O'):
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        move = best_move(board)
        board[move] = 'X'
        
        if check_winner(board, 'X'):
            print_board(board)
            print("AI wins! Better luck next time.")
            break

if __name__ == "__main__":
    play_game()
