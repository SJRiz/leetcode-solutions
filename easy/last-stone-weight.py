"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [stone*-1 for stone in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            prev = heapq.heappop(arr)
            prev2 = heapq.heappop(arr)
            heapq.heappush(arr, min(prev, prev2) - max(prev, prev2))
        
        return arr[0]*-1
    
    # Solution is O(nlog(n)) and O(n) space