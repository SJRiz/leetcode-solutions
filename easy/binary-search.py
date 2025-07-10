# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:

            # Half the index each time
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # If we undershoot, then we know everything to the left of the current middle (including the current middle) is also an undershoot
            elif nums[m] < target:
                l = m + 1
                
            # Likewise if we overshoot
            else:
                r = m - 1
        
        return -1