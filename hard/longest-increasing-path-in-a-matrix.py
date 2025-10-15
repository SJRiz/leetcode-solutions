from typing import List

"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(matrix)
        cols = len(matrix[0])

        cache = {}  # (r, c) -> number of elements before it

        def dfs(r, c):
            if (r, c) in cache:
                return cache[r,c]

            res = 0
            for dx, dy in dirs:
                if (0 <= r + dx < rows) and (0 <= c + dy < cols) and matrix[r+dx][c+dy] < matrix[r][c]:
                    res = max(res, dfs(r + dx, c + dy))
            res += 1
            cache[r,c] = res
            return res
        
        biggest = 0
        for r in range(rows):
            for c in range(cols):
                biggest = max(biggest, dfs(r, c))
        return biggest