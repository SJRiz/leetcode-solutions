"""
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.
"""

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # this question is so fucking poorly worded i thought it was a sliding window problem
        # turns out its just a delete duplicates and ignore negative numbers in a sum like the fuck bro
        
        hashset = set()
        sum = 0
        highest_num = float('-inf')

        for n in nums:
            highest_num = max(highest_num, n)

            if n not in hashset and n > 0:
                sum += n
                hashset.add(n)
        
        return highest_num if sum == 0 else sum
    
    # Solution is O(n) time and space
        