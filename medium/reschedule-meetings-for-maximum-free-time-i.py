# You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.
# You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].
# You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.
# The relative order of all the meetings should stay the same and they should remain non-overlapping.
# Return the maximum amount of free time possible after rearranging the meetings.
# Note that the meetings can not be rescheduled to a time outside the event.

class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        # Make an array of all time gaps
        gaps = [startTime[0]]
        for i in range(len(startTime) - 1):
            gaps.append(startTime[i+1] - endTime[i])
        
        gaps.append(eventTime - endTime[-1])

        # Make a sliding window of size k+1
        l = 0
        curr = 0
        largest = 0

        for r in range(len(gaps)):
            curr += gaps[r]
            if r >= k+1:
                curr -= gaps[l]
                l += 1
            
            # Save the largest from each window
            largest = max(largest, curr)

        return largest
    
    # Solution is O(n) time and space complexity