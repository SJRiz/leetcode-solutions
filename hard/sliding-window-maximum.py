# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array.
# The window slides one position to the right until it reaches the right edge of the array.
# Return a list that contains the maximum element in the window at each step.

from  typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # We will use a queue to track the greatest numbers (the biggest will be on the leftmost side)
        deq = deque()
        res = []

        left = 0
        for right in range(len(nums)):
            
            # Keep popping the list until the number is in the right spot
            # We do not have to worry about smaller numbers before the new big as the bigger number will be the local max for that
            # We only care about smaller numbers after the new big (trying to find its successor)
            while deq and nums[right] > deq[-1]:
                deq.pop()
                
            deq.append(nums[right])

            # If the window is the right size, then start saving the results
            if right >= k-1:
                res.append(deq[0])
                
                # Remove the max from the list if it is out of bounds
                if nums[left] == deq[0]:
                    deq.popleft()
                left += 1

        return res
    
    # Solution is O(n) time and O(n) space.