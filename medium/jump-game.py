from typing import List

"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # basically just avoid zeros
        # first pass: find indexes of zero.
        # second pass: see if there is a number that can jump over that zero
        # we can actually turn this into a sliding window: when we find a zero, close the window and see if a number exists
        # this works because we want to take the first number that can jump over the first zero. then when another zero comes up, we can check if that same number still works, if not, find another

        l = 0

        for r in range(len(nums)-1):
            if nums[r] == 0:
                found = False

                while l < r:
                    if l + nums[l] > r:
                        found = True
                        break
                    l += 1

                if found == False:
                    return False
        
        return True
        