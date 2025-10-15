from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # |----|  |--------|
        #   |------|
        # first insert the new interval to keep start points in ascending order O(n)
        # then merge all intervals O(n)
        res = []

        def check_merge(interval):
            if not res:
                res.append(interval)
            else:
                if res[-1][0] <= interval[0] <= res[-1][1] <= interval[1]:
                    res[-1][1] = interval[1]
                elif res[-1][1] < interval[0]:
                    res.append(interval)

        inserted = False

        for i in range(len(intervals)):
            if not inserted and newInterval[0] < intervals[i][0]:
                check_merge(newInterval)
                inserted = True
            check_merge(intervals[i])
        
        if not inserted:
            check_merge(newInterval)
        
        return res
    
    # Solution is O(n) time and O(1) extra space


