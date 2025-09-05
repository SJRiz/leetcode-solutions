"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
"""

from typing import List

class Solution:
    # We can first sum up the entire array O(n).
    # Then, we realize that both partitions must be half of this sum.
    # This problem is sorta similar to coin change
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        memo = set()

        for n in nums:
            total += n
        
        if total/2 != total//2:
            return False    # decimal number cant make with integers
        
        def knapsack(target, i):
            if target < 0 or (target, i) in memo or i == len(nums):
                return False
            if target == 0:
                return True
            
            memo.add((target, i)) # to stop recomputing values we already computed
            return knapsack(target - nums[i], i+1) or knapsack(target, i+1)

        return knapsack(total/2, 0) # if one subset can add up to the half, then we know 100% the other will be the other half