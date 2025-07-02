# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
# Return the maximum area of water that can be trapped between the bars.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Strategy: use two pointers; the purpose of both pointers is to find the largest height on the left and right side
        # Whatever pointer has the lowest height, prioritize maximizing that first
        # If the max height of any pointers change, we will calculate the area for the water there
        # We can do this by accumlating the heights, and subtracting it to the area between the 2 heights
        # The height accumlation and dist traveled will then reset

        left_accum = 0
        right_accum = 0
        left_dist = -1
        right_dist = -1
        left_max = 0
        right_max = 0

        total = 0

        left = 0
        right = len(height) - 1

        # We use <= because we do left += 1 at the end
        while left <= right:
            if left_max <= right_max:

                # If we find a new max height, add the rain water behind it
                if height[left] >= left_max:
                    # length*max height - accumlated heights gives the area of water
                    total += (left_max*left_dist - left_accum)
                    left_max = height[left]

                    # Reset the accumlated heights and distance covered
                    left_accum = 0
                    left_dist = -1
                else:

                    # If no new max height, accumlate it
                    left_accum += height[left]

                left_dist += 1
                left += 1
            
            # Exact same logic as above
            else:
                if height[right] >= right_max:
                    total += (right_max*right_dist - right_accum)
                    right_max = height[right]
                    right_accum = 0
                    right_dist = -1
                else:
                    right_accum += height[right]

                right_dist += 1
                right -= 1
        
        # At the end of the loop, we will know the 2 biggest heights, as well as the distance between them, and other heights accumlated in between.
        # We then calculate the last bit of water between these heights
        # The loop will end by either the left pointer going all the way to the right pointer or vice versa, meaning one of the accumlated sides and distance covered will be 0.
        # Thats why we use max to determine the non-zero value
        total += min(left_max, right_max)*max(left_dist, right_dist) - max(left_accum, right_accum)
        return total
    
    # Solution is O(n) time complexity and O(1) space.
    # I realized the solution can be simplified a lot further, by simply calculating the trapped water while moving the pointers, adding it to the total
    # But this approach was much more intuitive to me, and it is still optimal.