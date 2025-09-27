from typing import List

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
"""

class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        curr = 0
        best = 0
        res = 1

        for i in range(1, len(nums)-1):
            if (i - curr + nums[i]) >= (best - curr + nums[best]):
                best = i
            if (i - curr) == nums[curr]:
                res += 1
                curr = best
        return res