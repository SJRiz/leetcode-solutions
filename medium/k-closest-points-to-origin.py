"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

import math
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calc_dist(x, y):
            return math.sqrt((0 - x)**2 + (0 - y)**2)

        maxHeap = []

        for p in points:
            heapq.heappush(maxHeap, (calc_dist(p[0], p[1])*-1, p))
        
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        maxHeap = [x[1] for x in maxHeap]
        return maxHeap
    
    # Solution is O(nlog(k)) time and O(k) space