"""
You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.
"""

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        
        rows, cols = len(board), len(board[0])
        seen = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(start):
            stack = [start]
            visiting = set([start])
            touches_border = False
            
            while stack:
                x, y = stack.pop()
                
                # Check if this cell touches the border
                if x == 0 or x == rows-1 or y == 0 or y == cols-1:
                    touches_border = True
                    
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == "O" and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        visiting.add((nx, ny))
                        stack.append((nx, ny))
            
            # Flip to 'X' only if it doesn't touch the border
            if not touches_border:
                for x, y in visiting:
                    board[x][y] = "X"

        # Start DFS from every 'O' not yet seen
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in seen:
                    seen.add((r, c))
                    dfs((r, c))
