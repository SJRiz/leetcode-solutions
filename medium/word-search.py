"""
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Base cases: idx is out of bounds, next char not equal, string is too long, or string is equal to word
        res = False
        cache = set()

        def backtrack(row, col, s):
            nonlocal res
            if s == word:
                res = True
                return
            if (row, col) in cache or row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or len(s) > len(word) or (s and s[-1] != word[len(s)-1]) or res:
                return
            
            s += board[row][col]

            # Go right, go left, go up, or down.
            cache.add((row, col))
            backtrack(row + 1, col, s)
            backtrack(row - 1, col, s)
            backtrack(row, col + 1, s)
            backtrack(row, col - 1, s)
            cache.remove((row, col))

        # Do this for all letters
        for r in range(len(board)):
            for c in range(len(board[0])):
                backtrack(r, c, "")
        
        return res
    
    # Solution is O(n*4^m) time and O(m) space where m is the length of the word