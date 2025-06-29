# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
# You must write an algorithm that runs in O(n) time.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Turn the list into a hashset for O(1) lookups
        hashset = set(nums)

        # Track the largest count for each sequence
        largest_count = 0

        for n in hashset:

            # Do not bother if n-1 exists in the hashset already, we only care about the smallest number in the sequence
            if n-1 in hashset:
                continue

            # Count the sequence
            count = 1
            while n+count in hashset:
                count += 1

            # Save the largest count
            largest_count = max(count, largest_count)

        return largest_count
    
    # Solution is O(n) time.