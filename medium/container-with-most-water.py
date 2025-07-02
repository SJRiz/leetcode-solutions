# You are given an integer array heights where heights[i] represents the height of the i'th bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # We will use two pointers for this problem
        left = 0
        right = len(height) - 1

        area = 0

        while left < right:

            # We can calculate the current area by multiplying the smallest of the 2 heights by the distance between their indices
            current_area = min(height[left], height[right]) * (right - left)

            # If its larger than the current stored area, update it
            area = max(area, current_area)

            # The core idea here is that when we start at the largest width, and start decreasing the width, the only way to increase the area would be to maximize or increase the height.
            # Since the area of the container is bounded to the smallest of the 2 heights, we want to try and increase the height that is bounding the area
            # (e.g.  2,3 2,4 2,5 2,6 all would be simplified to just 2. Instead of trying to increase the right height, we try to increase the left, or 2 in this case)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area
    
    # Solution is O(n) time, and O(1) space complexity. I'm proud that I was able to figure this out intuitively 