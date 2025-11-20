from typing import List
import heapq

"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # ----------------------------
        #   ------------
        #        -------------
        #         ----
        #                  ---------

        # keep track of smallest end point maybe? and if a start is greater than smallest endpoint then update

        days = 0
        minheap = []
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if minheap:
                smallest_end = minheap[0]
                if interval.end <= smallest_end:    # interval is directly within 
                    days += 1
                elif interval.start < smallest_end and interval.end > smallest_end: # interval is partially in
                    days += 1
                if interval.start >= smallest_end:  # interval is disjoint
                    heapq.heappop(minheap)
            else:
                days += 1
            
            heapq.heappush(minheap, interval.end)
        
        return days