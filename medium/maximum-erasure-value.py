"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
"""

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Sliding window + max sum of the window
        window = set()
        l = 0
        window_sum = 0
        max_sum = 0

        for n in nums:
            window_sum += n
            if n in window:
                while True:
                    window_sum -= nums[l]
                    window.remove(nums[l])
                    if nums[l] == n:
                        l+=1
                        break
                    l += 1

            window.add(n)
            max_sum = max(max_sum, window_sum)

        return max_sum
    
    # Solution is O(n) time and O(m) space where m is the longest unique subseq