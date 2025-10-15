from typing import List

"""
Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.
"""

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # its basically a 2d dp but we can just track the biggest sum for mod 0, 1, 2
        maxs = [0, 0, 0]

        for n in nums:
            buffer = [0, 0, 0]
            for mod in maxs:
                new = n + mod
                buffer[new%3] = max(buffer[new%3], maxs[new%3], new)    # see if adding the current sum to the largest of that mod sum will create a sum even larger than one in a another mod sum. also check if the buffer already found the biggest one

            for i in range(len(buffer)):
                maxs[i] = max(maxs[i], buffer[i])

        return maxs[0]