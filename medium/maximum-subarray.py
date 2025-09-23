from typing import List

"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sweep through array
        # if the sum becomes negative, start another sequence
        
        res = float("-inf")
        curr = 0

        for n in nums:
            curr += n
            res = max(res, curr)
            if curr < 0:
                curr = 0    # reset
        
        return res
    
    # O(n) time and O(1) space