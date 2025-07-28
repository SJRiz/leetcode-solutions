"""
Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack(idx, stack):
            if not stack:
                res.append(sol[:])
                return

            if idx == len(stack):
                return
            
            # Go next
            backtrack(idx + 1, stack[:])

            # Or use this index and shorten the stack
            sol.append(stack[idx])
            stack.pop(idx)
            backtrack(0, stack)
            sol.pop()

        backtrack(0, nums)

        return res
    
    # Solutions is O(n * n!) time and O(n) space. Can be simplified by using a for loop, and removing the chosen value from the for loop from the remaning list
            
