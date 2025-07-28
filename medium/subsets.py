"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack(idx):
            if idx == len(nums):
                res.append(sol[:])
                return None
            
            # Skip
            backtrack(idx + 1)

            # Add element (simulate a recursive call stack)
            sol.append(nums[idx])
            backtrack(idx + 1)
            sol.pop()
        
        backtrack(0)
        return res
    
    # Solution is O(2^n) time and O(n) space for recursion stack