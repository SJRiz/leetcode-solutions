# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use O(1) additional space.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Use a left and right pointer
        left = 0
        right = len(numbers) - 1

        while left < right:
            # If the sum of the pointer index is too big, the right pointer should go left (this will decrease the sum)
            if numbers[left] + numbers[right] < target:
                left += 1

            # If the sum of the pointer index is too small, move the left point right (increase sum)
            elif numbers[left] + numbers[right] > target:
                right -= 1

            # Keep shifting them until they eventually reach the target value
            else:
                return [left+1, right+1]
            
    # Solution is O(n) time.