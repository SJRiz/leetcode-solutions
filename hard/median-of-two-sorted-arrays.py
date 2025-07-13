# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Binary search the smaller array (arr1)
        arr, arr2 = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        l, r = 0, len(arr) - 1

        while True:
            # Partition index of the smaller array (Every value to the left of the partition inclusive will be smaller than the median)
            # Likewise, values to the right of the parition index will be larger
            part1 = (l + r) // 2

            # Fill the remaning empty portion of the partitions (Note this partition index is actually inclusive to the larger values)
            part2 = (len(nums1) + len(nums2)) // 2 - (part1 + 1)

            # Values to the left and right of each partition. Also edge cases to handle parition values out of bounds
            left_part1 = float("-inf") if part1 < 0 else arr[part1]
            right_part1 = float("inf") if part1 >= len(arr) - 1 else arr[part1 + 1]
            right_part2 = float("inf") if part2 > len(arr2) - 1 else arr2[part2]
            left_part2 = float("-inf") if part2 < 1 else arr2[part2 - 1]

            # If we have a valid partition, then we have an answer (which will depend on if the total length of both arrays are even or edd)
            if left_part1 <= right_part2 and left_part2 <= right_part1 :
                if (len(arr) + len(arr2)) % 2 == 0:
                    return (max(left_part1, left_part2) + min(right_part2, right_part1))/float(2)
                else:
                    return min(right_part1, right_part2)
            
            # Otherwise move the partition left or right depending on what side of the partition dissatisfies the partition
            elif left_part1 > right_part2:
                r = part1 - 1
            else:
                l = part1 + 1

    # Solution is O(min(log(n), log(m))) time and O(1) space.