# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # There will be 2 portions of the list: a bigger sorted list, and a smaller sorted list
        # Every middle, check what portion we are on, and see if the target is in the range,
        # if not then we know the target will never be in that range and adjust the pointer

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # Check if on smaller sorted list (right side)
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

            # Other check bigger sorted list (left side)
            else:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
        
        return -1