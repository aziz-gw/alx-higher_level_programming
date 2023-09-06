#!/usr/bin/python3

"""
Solves the N-queens puzzle.

Determines all possible solutions to placing N non-attacking queens
on an NxN chessboard.
"""
import sys


def initialise_board(n):
    """
    Initialise an `n`x`n` chessboard with empty cells.
    """
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def copy_board(board):
    """
    Create a deep copy of the chessboard.
    """
    return [row[:] for row in board]


def find_queen_positions(board):
    """
    Extract the positions of queens from the board.
    """
    positions = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                positions.append([r, c])
    return positions


def mark_attacked_cells(board, row, col):
    """
    Mark cells where queens can't be placed.
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve_queens(board, row, queens, solutions):

    """
    Recursively solve the N-queens puzzle.
    """
    if queens == len(board):
        solutions.append(find_queen_positions(board))
        return solutions
    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = copy_board(board)
            tmp_board[row][col] = "Q"
            mark_attacked_cells(tmp_board, row, col)
            solutions = solve_queens(tmp_board, row + 1, queens + 1, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initialise_board(N)
    solutions = solve_queens(board, 0, 0, [])
    for solution in solutions:
        print(solution)
