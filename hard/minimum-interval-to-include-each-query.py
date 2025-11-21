from typing import List
import heapq

"""
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.
"""

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # question is asking to find the smallest interval that contains a query point basically
        #      ----
        # ------
        #   --

        #


        res = [-1] * len(queries)
        qs = [(q, i) for i, q in enumerate(queries)]
        qs.sort()

        intervals.sort()

        hq = []
        idx = 0
        interval = intervals[idx]

        for q, i in qs:
            
            while idx < len(intervals) and intervals[idx][0] <= q:
                start, end = intervals[idx]
                heapq.heappush(hq, (end - start + 1, end))
                idx += 1

            while hq and q > hq[0][1]:
                heapq.heappop(hq)
            
            res[i] = hq[0][0] if hq else -1
        
        return res
            




