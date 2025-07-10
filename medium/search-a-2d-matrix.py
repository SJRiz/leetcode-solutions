# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # We can just think of this as a giant 1D array
        # Create a helper function to turn a 1D index into a 2D
        def convert_to_2d(num):
            return (num // len(matrix[0]), num % len(matrix[0]))

        # Apply the binary search algo as usual
        l, r = 0, (len(matrix)) * (len(matrix[0])) - 1
        while l <= r:
            m = (l + r) // 2
            row, col = convert_to_2d(m)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False