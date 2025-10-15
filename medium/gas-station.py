from typing import List

"""
There are n gas stations along a circular route. You are given two integer arrays gas and cost where:

gas[i] is the amount of gas at the ith station.
cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)
You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.

It's guaranteed that at most one solution exists.
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [1,2,3,4], cost = [2,2,4,1]
        # to get past station 0, you need > 2 gas (net = -1).
        # to get past station 1, you need > 2 gas (net = 0).
        # to get past station 2, you need > 4 gas. (net = -1)
        # to get past station 3, you need > 1 gas. (net = 3)

        # this loop will increase infinity and if we start at station 3, we can pass all requirements
        # strat: start at the position where our net will START increasing the most.
        # KADANES ALGORITHM

        res = 0
        idx = 0
        tot = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]
            tot += net

            res += net
            if res < 0:
                res = 0
                idx = i+1
        
        return -1 if tot < 0 else idx

