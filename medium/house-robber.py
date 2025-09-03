"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

from typing import List

class Solution:
    # for every ith house, the most money you can get is either cum sum from i-2 + i,
    # or cum sum from i-1
    # we only care about the latest 2 subproblems
    
    def rob(self, nums: List[int]) -> int:
        last = 0            # i-1
        second_last = 0     # i-2

        for n in nums:
            last, second_last = max(second_last + n, last), last
        
        return last
