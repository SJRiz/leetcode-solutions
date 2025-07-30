"""
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.
"""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sol = [], []

        def backtrack(idx):
            if idx == len(nums):
                res.append(sol[:])
                return
            
            # Two options, use current num, or skip until the next unique
            sol.append(nums[idx])
            backtrack(idx + 1)
            sol.pop()

            while idx < len(nums)-1 and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1)

        backtrack(0)
        return res
    
    # Solution is O(n * 2^n) time and O(n) space