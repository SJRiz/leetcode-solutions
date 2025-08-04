"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # check whether going from 0 to n-1 or 1 to n is bigger
        
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0
        rob3, rob4 = 0, 0

        for i in range(len(nums) - 1):
            rob1, rob2 = rob2, max(rob2, rob1 + nums[i])
            rob3, rob4 = rob4, max(rob4, rob3 + nums[-i-1])
        
        return max(rob2, rob4)