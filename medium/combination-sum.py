"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(idx, s):
            # Base cases: Either too big/small (return None and backtrack) or equals target (append to res)
            nonlocal res, sol

            if s == target:
                res.append(sol[:])
                return None

            if idx == len(nums) or s > target:
                return None
            
            # Go next
            backtrack(idx + 1, s)

            # Add current
            sol.append(nums[idx])
            backtrack(idx, s + nums[idx])
            sol.pop()
        
        backtrack(0,0)
        return res
    
    # Solution is O(2^n) time and O(n) space