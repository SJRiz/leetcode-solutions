"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
"""

from typing import List

class Solution:
    # for every number n, look for a number less than n with the biggest LIS (m) through the memo
    # the LIS of n would be the LIS of m plus 1.

    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        res = 0

        for i in range(len(nums)):
            before = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    before = max(before, memo[j])

            memo[i] = before + 1
            res = max(res, memo[i])

        return res
