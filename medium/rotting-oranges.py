"""
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.
"""

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        row = len(grid)
        col = len(grid[0])

        deq = deque()
        seen = set()
        
        cnt = 0
        available = 0

        # find all rotten fruits first, and keep track of normal fruits
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    deq.append((r,c))
                    seen.add((r,c))
                elif grid[r][c] == 1:
                    available += 1
        
        if not available:
            return 0   # end early

        while deq:
            cnt += 1
            for _ in range(len(deq)):
                x, y = deq.popleft()

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                        available -= 1
                        grid[nx][ny] = 2
                        seen.add((nx, ny))
                        deq.append((nx, ny))
                        
            if not available:
                break   # no need to continue bfs if all are rotten
        
        return cnt if not available else -1
    
    # Solution is O(n*m) time and space where n*m is the area of the graph