# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # First, count all the elements using a hashmap
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        # Create up to len(nums) buckets. The count of each element will be their index in the bucket
        buckets = [[] for _ in nums]
        for num, count in hashmap.items():
            # Elements with the highest count will be in the first indexes
            buckets[len(buckets) - count].append(num)

        result = []
        
        # Keep appending to the results array until we reach k elements
        # Since we stop at k elements, this is bounded by O(n) despite having 2 for loops
        for bucket in buckets:
            for num in bucket:
                result.append(num)
                if len(result) >= k:
                    return result
        
        return result
    
    # Time complexity is O(n).