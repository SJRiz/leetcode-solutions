from typing import List

"""
You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
"""

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # fuck my chungus life bro fuck everything
        cuts = 0

        intervals.sort(key=lambda x: (x[1], -x[0]))

        c1, c2 = 0, 0

        for start, end in intervals:
            if not cuts or start > c2:
                cuts += 2
                c2 = end
                c1 = end-1
            
            if start > c1 and end >= c2:
                c1 = c2
                c2 = end
                cuts += 1

        return cuts


            


