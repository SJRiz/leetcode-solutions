# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort the array first. Python's sort method is O(n*logn). This will allow us to use 2 pointers to search for a sum
        nums.sort()
        results = []

        # We will track current numbers to avoid duplicates
        curr = None

        for i in range(len(nums) - 2):
            if curr != nums[i]:
                curr = nums[i]

                # Everytime we loop through the list, we will use 2 pointers where the left starts at i + 1
                # We want to find 2 numbers that add up to -nums[i] for each unique nums[i]
                left = i + 1
                right = len(nums) - 1

                # Track left and right values to avoid duplicates
                left_curr = None
                right_curr = None

                while left < right:
                    # nums[i] + nums[j] + nums[k] = 0, so nums[j] + nums[k] = -nums[i]
                    target = -curr

                    # Two sum sorted array logic
                    if nums[left] + nums[right] < target:
                        left += 1
                    elif nums[left] + nums[right] > target:
                        right -= 1
                    else:

                        # If the left and right values are different from previous iterations, add it
                        if left_curr != nums[left] and right_curr != nums[right]:
                            left_curr = nums[left]
                            right_curr = nums[right]
                            results.append([nums[i], nums[left], nums[right]])

                        # Nudge the pointers to keep iterating and looking for sums
                        # If there is another sum, they should be right next to the current left and right pointers
                        left += 1
                        right -= 1

        
        return results
    
    # Solution is O(n^2) time, which is the most optimal.