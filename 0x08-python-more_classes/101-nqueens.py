#!/usr/bin/python3

"""Solving the The N queens puzzle"""

import sys


def is_convertible_to_int(s):
    """Helper function to convert argv[1] to integer"""

    if not s:
        return False

    for char in s:
        if not char.isdigit():
            return False

    return True


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    Returns True if safe, False otherwise
    """
    # Check the left side of this row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N Queens problem and print all possible solutions
    """
    def solve(board, col):
        if col >= N:
            # All queens are placed, print the solution
            solution = []
            for row in range(N):
                for c in range(N):
                    if board[row][c] == 1:
                        solution.append([row, c])
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, col + 1)
                board[row][col] = 0  # Backtrack

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    length = len(sys.argv)
    if length != 2:
        print("Usage: nqueens N")
        exit(1)

    N = sys.argv[1]
    if not is_convertible_to_int(N):
        print("N must be a number")
        exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    solve_nqueens(N)
