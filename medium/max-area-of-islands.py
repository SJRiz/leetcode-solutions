"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        dirs = [(1,0), (-1,0), (0,1),(0,-1)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    cnt = 1
                    grid[r][c] = 0

                    # bfs
                    deq = deque([(r,c)]) # a node is a tuple of r, c
                    while deq:
                        node = deq.popleft()
                        for dr in dirs:
                            x, y = node[0] + dr[0], node[1] + dr[1]
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                                cnt += 1
                                grid[x][y] = 0
                                deq.append((x, y))

                    # keep track of max, always
                    res = max(res, cnt)
        
        return res
    
    # Solution is O(n*m) time and space where n*m is the area of the graph
                