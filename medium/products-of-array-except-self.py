# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Do not use division and aim for O(n)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Prefix and suffix products
        Lprod = [1]
        Rprod = [1]

        # Populate the left and right product lists
        for i in range(len(nums)-1):
            Lprod.append(Lprod[i] * nums[i])
            Rprod.append(Rprod[i] * nums[len(nums)-1-i])

        # You can construct each output by combining the left and right product lists
        # Rprod is populated in reverse order, so you must index starting from the very end
        result = []
        for i in range(len(Lprod)):
            result.append(Lprod[i] * Rprod[len(Lprod)-1-i])


        return result
    
    # Solution is O(n) time. I was able to figure this solution out without knowing what prefix or suffix sums were beforehand

