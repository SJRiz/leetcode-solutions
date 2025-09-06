"""
You are given a 
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
"""

from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we do a bfs on every grid point and search for the nearest treasure.
        # stop the path if it hits a -1
        # use the minimum count (every iteration is a step outward)

        seen = set()
        dirs = [[1,0],[-1,0], [0,1],[0,-1]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    seen = set((r, c))
                    depth = 0
                    deq = deque([(r, c)])
                    found = False

                    # bfs
                    while deq:
                        depth += 1
                        for _ in range(len(deq)):
                            x, y = deq.popleft()
                            for dx, dy in dirs:
                                new_x, new_y = x + dx, y + dy
                                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != -1 and (new_x, new_y) not in seen:
                                    seen.add((new_x, new_y))
                                    deq.append((new_x, new_y))
                                    if grid[new_x][new_y] == 0:
                                        found = True
                        
                        if found == True:
                            break
                    
                    grid[r][c] = depth if depth else grid[r][c]

    # Solution is O(a^2) time and O(a) space where a is the area of the grid
    # tho this can easily be optimized by only doing bfs on every treasure chest instead