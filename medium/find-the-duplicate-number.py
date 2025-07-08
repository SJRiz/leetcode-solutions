# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and using only constant extra space.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Every number in the list can point to another in the list (each "node" points to another index)
        # We can then use the Floyd cycle detection algorithm to find the beginning of the cycle

        # First, check where the slow and fast pointer intersect
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Then, continue the slow pointer through the cycle while moving a new slow pointer. Wherever they intersect is where the cycle starts
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2

    # Solution is O(n) time and O(1) space complexity