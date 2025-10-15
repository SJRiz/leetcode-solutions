"""
Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.
"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # first pass: mark all zeros
        # second pass look for the marks and set adjacent  rows and cols equal 0

        width = len(matrix)
        height = len(matrix[0])

        def put_zeros(row, col):
            for i in range(width):
                if matrix[i][col] != "M":
                    matrix[i][col] = 0
            for i in range(height):
                if matrix[row][i] != "M":
                    matrix[row][i] = 0

        for r in range(width):
            for c in range(height):
                if matrix[r][c] == 0:
                    matrix[r][c] = "M"

        for r in range(width):
            for c in range(height):
                if matrix[r][c] == "M":
                    matrix[r][c] = 0
                    put_zeros(r,c)
        

        