# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
    # 1. Each row must contain the digits 1-9 without duplicates.
    # 2. Each column must contain the digits 1-9 without duplicates.
    # 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

# Return true if the Sudoku board is valid, otherwise return false

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # A set for each rule, if there are any duplicates, then we know its invalid
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        for row in range(9):
            for col in range(9):

                # Check every element, and see if it exists in one of the sets already
                if board[row][col] != ".":
                    if board[row][col] in col_set[col] or board[row][col] in row_set[row] or board[row][col] in square_set[(row // 3, col // 3)]:
                        return False
                    
                    # If not, add it to the set
                    row_set[row].add(board[row][col])
                    col_set[col].add(board[row][col])

                    # The 3x3 or "subsquares" can be represented as an x,y tuple with floor division to group the numbers in these squares
                    square_set[(row // 3, col // 3)].add(board[row][col])

        return True