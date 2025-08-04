"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        memo[0] = 1

        for i in range(1, n+1):
            res = 0
            
            res += memo[i - 1]
            if i - 2 >= 0:
                res += memo[i - 2]

            memo[i] = res

        return res
    
    # O(n) time and space. Can be optimized to O(1) space however by cleverly tracking the last 2 numbers