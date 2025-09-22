from typing import List

"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic increasing stack of heights. track index also. everytime we pop, check area relative to index.
        # the new element in the stack will take the index or "width" of the previous smallest

        mins = []   # (minimum, index)
        res = 0

        for i in range(len(heights)):
            w = i
            while mins and heights[i] < mins[-1][0]:
                m, w = mins.pop()
                res = max(res, m*(i-w))
            mins.append((heights[i], w))
        
        # clear it
        while mins:
            m, w = mins.pop()
            res = max(res, m*(len(heights)-w))

        
        return res

    # Solution is O(n) time and space

