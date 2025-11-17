from functools import lru_cache

"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 2^5 -> 24 * 2 -> 
        
        @lru_cache(None)
        def p(a):
            if a == 1:
                return x
            if a % 2 == 1: # odd number
                return p((a-1)) * x
            else:
                return p(a/2) * p(a/2)
        
        if n == 0:
            return 1
        if x == 0:
            return 0

        if n < 0:
            return 1/(p(-1*n))
        else:
            return p(n)



