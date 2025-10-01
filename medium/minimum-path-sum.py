from typing import List

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # to get to every grid point, you either come from the left or from above
        # the sum for every i, j point is just the minimum of i-1, j-1 + curr
        rows = len(grid)+1
        cols = len(grid[0])+1
        dp = [[float("inf")]*cols for _ in range(rows)]
        dp[1][1] = grid[0][0]

        for r in range(1, rows):
            for c in range(1, cols):
                if not (r == 1 and c == 1):
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r-1][c-1]

        return dp[-1][-1]
    
    # Solution is O(n*m) time and space