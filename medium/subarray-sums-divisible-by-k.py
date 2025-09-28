from typing import List

"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # idea: we first start by doing a prefix sum.
        # if we wanna find a contigious subarray that has a sum divisible by 5, we can find that specific subarray by subtracting a smaller prefix sum by a larger one.
        # with the idea above, its possible to calculate every single subarray.
        # next, we have to find such combination where the subarray has a sum divisble by k
        # a.k.a, (a - b) % k = 0.
        # using math properties: (a % k) - (b % k) = 0, or a % k = b % k. so you just need to find prefix sums where its remainders are the same.
        # final note: you must consider ALL pairs. (so this would look like 1 + 2 + 3 + 4 everytime you find another identical remainder, use a hashmap to track)
        # always add 1 to the total if you encounter a 0

        cum = 0
        seen = {}
        tot = 0

        for n in nums:
            cum += n
            res = cum % k

            if res == 0:
                tot += 1
            if res in seen:
                tot += seen[res]
                seen[res] += 1
            else:
                seen[res] = 1
        
        return tot
        
