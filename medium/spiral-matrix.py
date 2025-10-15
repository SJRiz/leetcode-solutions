"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        w = len(matrix)       # rows
        h = len(matrix[0])    # cols
        l, r = 0, h - 1
        t, b = 0, w - 1

        while l <= r and t <= b:
            # top
            for i in range(l, r + 1):
                res.append(matrix[t][i])

            # right
            for i in range(t + 1, b + 1):
                res.append(matrix[i][r])

            if t < b:  # bottom row exists
                for i in range(r - 1, l - 1, -1):
                    res.append(matrix[b][i])

            if l < r:  # left col exists
                for i in range(b - 1, t, -1):
                    res.append(matrix[i][l])

            l += 1
            r -= 1
            t += 1
            b -= 1

        return res
