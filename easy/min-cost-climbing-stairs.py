from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # suppose we are at the last ith index of the stairwell
        # to get to that last ith index, we either had to step from the i - 1 or i - 2 step.
        # the step that has the least accumalated cost is the step we came from

        memo = [0] * (len(cost)+1)    # account for the base case

        for i in range(2, len(cost)+1):
            memo[i] = min(memo[i-1] + cost[i-1], memo[i-2] + cost[i-2])
        
        return memo[-1]
    
    # Solution is O(n) time and space