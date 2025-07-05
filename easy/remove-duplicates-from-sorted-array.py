# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 1
        for right in range(1, len(nums)):

            # If the prev index value is different from the current, that means its a new number
            if nums[right] != nums[right - 1]:
                nums[k] = nums[right]
                k += 1 
        
        return k
    
    # Solution is O(n) time