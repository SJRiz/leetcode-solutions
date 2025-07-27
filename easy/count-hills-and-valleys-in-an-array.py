"""
You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.
"""

from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev = None
        count = 0

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]

            # If the previous difference and current difference have opposing signs and aren't zero, then its either a hill or valley
            if prev and min(diff, prev) < 0 and max(diff, prev) > 0:
                count += 1

            # Only record previous difference if not zero
            if diff != 0:
                prev = diff
        
        return count
    
    # Solution is O(n) time and O(1) space.
            

                    