from collections import defaultdict
from typing import List

class CountSquares:
    # to count squares we can use arrow method
    # first check (x+n), (x+n). if point exists, check (x+n, y) and (x, y+n).
    # for dupes: we do crazy math (just multiply all number of points together)

    def __init__(self):
        self.storage = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.storage[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        # this time we only count over KNOWN points
        # we will do this by checking if the slope between the point and the iterated point is |1|.
        # if its one, then check if there exists a point in (x+dx, y) and (x, y+dy). if yes, multiply their values
        # ^ you actually dont have to check if that point exists. The 0 multiplication will make up for it

        res = 0
        
        def safe_check(x, y):
            return self.storage[(x,y)] if (x,y) in self.storage else 0

        for x, y in self.storage:
            dx, dy = x - point[0], y - point[1]
            if dx == 0:
                continue
            if abs(dy/dx) == 1:
                res += safe_check(point[0] + dx, point[1] + dy)*safe_check(point[0] + dx, point[1])*safe_check(point[0], point[1] + dy)
        
        return res
