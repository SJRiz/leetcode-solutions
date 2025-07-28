"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        candidates.sort()

        def backtrack(idx, s):
            if s == target:
                res.append(sol[:])
                return None
            if s > target or idx == len(candidates):
                return None
            
            # Add current index and go next
            sol.append(candidates[idx])
            backtrack(idx + 1, s + candidates[idx])
            sol.pop()

            # Skip to the next unique
            while idx < len(candidates)-1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(idx + 1, s)
        
        backtrack(0, 0)
        return res
    
    # Solution is O(n * 2^n) time and O(n) space