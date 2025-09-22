from typing import List

"""
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we need to sort based on position
        # idea: if a car reaches the target destination in less time than the car ahead of it, then it'll be part of a fleet of that car
        # we will do a monotonic decreasing stack

        def safe_divide(num, denom):
            if denom == 0:
                return float("inf")
            else:
                return num/denom

        pairs = [(position[i], safe_divide((target-position[i]), speed[i])) for i in range(len(position))]
        pairs.sort()

        stk = []

        for _, time in pairs:
            while stk and time >= stk[-1]:
                stk.pop()
            stk.append(time)
        
        return len(stk)
            