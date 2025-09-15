"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

import math
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        layer = 0   # track which "ring" of the matrix we're rotating

        while n > 1:
            for i in range(n - 1):
                # calculate positions relative to the current layer
                top = matrix[layer][layer + i]
                right = matrix[layer + i][layer + n - 1]
                bottom = matrix[layer + n - 1][layer + n - 1 - i]
                left = matrix[layer + n - 1 - i][layer]

                # perform 4-way swap
                matrix[layer][layer + i] = left
                matrix[layer + i][layer + n - 1] = top
                matrix[layer + n - 1][layer + n - 1 - i] = right
                matrix[layer + n - 1 - i][layer] = bottom

            # shrink problem size: go one layer inward
            layer += 1
            n -= 2

    # Solution is O(n^2) time and O(1) space