from typing import List

"""
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
"""

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        inc = 1
        dec = 0
        longest = 0

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                inc = inc+1 if not dec else 2
                dec = 0
            elif arr[i] < arr[i-1]:
                dec += 1
                if inc > 1:
                    longest = max(longest, inc + dec)
            else:
                dec = 0
                inc = 1
        
        return longest