from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # sort, compare start intervals
        intervals.sort(key=lambda x: (x[0], x[1]))
        print(intervals)

        prev = None # (start, end)
        res = 0

        for start, end in intervals:
            if prev == None or start >= prev[1]:
                prev = (start, end)
            else:
                res += 1
                # prioritize the interval with the smaller length
                if end <= prev[1] and prev[1] - prev[0] > end - start:
                    prev = (start, end)
        
        return res
        