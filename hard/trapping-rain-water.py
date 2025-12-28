# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
# Return the maximum area of water that can be trapped between the bars.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        curr = min(height[l], height[r])    # the "water level"
        area = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if curr - height[l] < 0:
                    curr = min(height[l], height[r])
                else:
                    area += curr - height[l]
            else:
                r -= 1
                if curr - height[r] < 0:
                    curr = min(height[l], height[r])
                else:
                    area += curr - height[r]
        
        return area
    
    # O(n) time O(1) space