from typing import List

"""
You are given an array of integers nums and an integer target.

For each number in the array, you can choose to either add or subtract it to a total sum.

For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the expression such that the total sum equals target.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(idx, cum):
            if idx == len(nums):
                if cum == target:
                    return 1
                return 0
            if (idx, cum) in memo:
                return memo[(idx, cum)]

            pos = dfs(idx + 1, cum + nums[idx])
            neg = dfs(idx + 1, cum - nums[idx])

            memo[(idx, cum)] = pos + neg
            return memo[(idx, cum)]

        return dfs(0, 0)