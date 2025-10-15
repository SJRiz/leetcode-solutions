"""
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0

        # do a dfs on every 1 thats not in the seen
        def dfs(row, col):
            if (row, col) in seen or not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])) or grid[row][col] == "0":
                return
            
            seen.add((row, col))

            # check neighbours
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in seen and grid[row][col] == "1":
                    res += 1
                    dfs(row, col)
        
        return res
    
    # Solution is O(n * m) time and space where n * m is the area of the grid