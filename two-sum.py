# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Use a hashmap for O(1) lookup
        hashmap = {}

        for j, num in enumerate(nums):

            # The second number is always target - first, see if it exists in the hashmap
            needed_num = target - num
            if needed_num in hashmap:

                # hashmap[needed_time] will always be smaller than the iterated value of the list (since you are searching for values you already searched before)
                return [hashmap[needed_num], j]
            else:
                
                # Store the value to the hashmap to check later
                hashmap[num] = j

# O(n) time complexity, O(n) space complexity
