"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        from_pacific = set()
        from_atlantic = set()

        def iterative_dfs(ocean, node):
            stack = [node]
            ocean.add(node)

            while stack:
                x, y = stack.pop()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if ((nx, ny) not in ocean
                    and 0 <= nx < len(heights) and 0 <= ny < len(heights[0])
                    and heights[nx][ny] >= heights[x][y]):
                        ocean.add((nx, ny))
                        stack.append((nx, ny))
        
        # all pacifics:
        for r in range(len(heights)):
            iterative_dfs(from_pacific, (r, 0))
        for c in range(len(heights[0])):
            iterative_dfs(from_pacific, (0, c))

        # all atlantics:
        for r in range(len(heights)):
            iterative_dfs(from_atlantic, (r, len(heights[0]) - 1))
        for c in range(len(heights[0])):
            iterative_dfs(from_atlantic, (len(heights) - 1, c))

        return list(set.intersection(from_pacific, from_atlantic))
    
    # Solution is O(n*m) time and space where n*m is the area of the grid