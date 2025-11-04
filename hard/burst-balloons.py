from functools import lru_cache
from typing import List

"""
You are given an array of integers nums of size n. The ith element represents a balloon with an integer value of nums[i]. You must burst all of the balloons.

If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.

Return the maximum number of coins you can receive by bursting all of the balloons.
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dfs(start, end):
            if start - end == 1:
                return 0

            res = 0
            for i in range(start+1,end):
                best_left = dfs(start, i)
                best_right = dfs(i, end)

                res = max(res, best_left + best_right + nums[start]*nums[i]*nums[end])
            return res
        
        nums.append(1)
        nums.insert(0, 1)
        return dfs(0, len(nums)-1)