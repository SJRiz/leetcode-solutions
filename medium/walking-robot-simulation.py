from collections import defaultdict
from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dist = 0

        # dirs: (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0) -> ...
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr = (0, 0)
        dir_index = 0   # turn right means add 1, left means sub 1

        # turn obstacle into hashmap
        hm_x = defaultdict(set)
        for x, y in obstacles:
            hm_x[x].add(y)

        for c in commands:
            if c == -1:
                dir_index = (dir_index+1)%4
            elif c == -2:
                dir_index = (dir_index-1)%4
            else:
                for i in range(c):
                    movement = (curr[0] + dirs[dir_index][0], curr[1] + dirs[dir_index][1])
                    if movement[0] in hm_x and movement[1] in hm_x[movement[0]]:
                        break
                    else:
                        curr = movement
                        dist = max(dist, curr[0]*curr[0] + curr[1]*curr[1])
        
        return dist
