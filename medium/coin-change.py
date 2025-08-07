"""
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # suppose we had coins [1,2,5] and amount = 13
        # the least amount of coins to make 13 would be the minimum of the ways to make 12, 11, and 8.
        # each of which also has their own sub problem (i.e. least amount to make 8 is minimum to make 7, 6, and 3)

        sub_problems = [-1] * (amount+1)
        sub_problems[0] = 0     # going from any number to 0 would be exactly one way (example 3 - 3, 1 - 1)

        for i in range(1, amount+1):
            res = float("inf")
            for coin in coins:
                if i - coin >= 0 and sub_problems[i-coin] != -1:
                    res = min(res, sub_problems[i-coin])
            
            if res != float("inf"):
                sub_problems[i] = res + 1
        
        return sub_problems[-1]
    
    # Solution is O(n * m) time and O(m) space where n is the number of coins and m is the amount

