from typing import List

"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we create a stack s.t. the bottom of the stack is the highest temperature, and goes up in decreasing order
        # we take note of the index of the temperature. if we insert a new temp and its higher than previous values of the stack, pop it.
        # ^ in the res array, append the difference of the indexes of the popped temperature

        stk = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                j = stk.pop()
                res[j] = i-j
            stk.append(i)
        
        return res
    
    # Solution is O(n) time and O(n) extra space