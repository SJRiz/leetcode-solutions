# Given an integer array `nums`, return `true` if any value appears at least twice. Otherwise, return `false`.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Create a hashmap that will be used to store numbers we already checked
        count = {}

        for num in nums:
            # Go through the list and see if that position was already on the hashmap
            # Hashmaps have O(1) lookup so it is ideal
            if num in count:
                return True
            else:
                count[num] = 0

        # If we went through the whole array without returning True, then there must have been no duplicates.
        return False