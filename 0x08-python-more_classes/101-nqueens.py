#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if placing a queen at the given row and column is safe.
    Args:
        board (list): The current board configuration.
        row (int): The row to check.
        col (int): The column to check.
    Returns:
        bool: True if it is safe to place a queen at
        (row, col), False otherwise.
    """

    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def nqueens(N, board, row):

    """
    Recursive function to find all possible
    solutions for N Queens problem.

    Args:
        N (int): The size of the chessboard and the
        number of queens to place.

        board (list): The current board configuration.
        row (int): The current row being considered.
    """

    if row == N:
        print([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                nqueens(N, board, row + 1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: ./nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    board = [-1] * N
    nqueens(N, board, 0)
