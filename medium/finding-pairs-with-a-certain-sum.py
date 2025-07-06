# You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:
    # Add a positive integer to an element of a given index in the array nums2.
    # Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).

# Implement the FindSumPairs class:
    # FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
    # void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
    # int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.

from collections import defaultdict

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2

        # nums2.length >>> nums1.length, so we want to constantly keep track of the count of each num in nums2 in a hashmap for O(1) lookup
        self.num2count = defaultdict(int)
        for num in nums2:
            self.num2count[num] += 1

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # Update the counter as well
        self.num2count[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.num2count[self.nums2[index]] += 1
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        count = 0

        # Do a two-sum algorithm. Loop through nums1 because its smaller
        for num in self.nums1:
            if tot - num in self.num2count:
                count += self.num2count[tot - num]

        return count
        