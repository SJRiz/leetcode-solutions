from typing import List

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        # example amount = 10, coins = [1, 2, 5]
        # check possible ways with just 1, then just 1 and 2, then just 1 and 2 and 5
        # in the for loop below, first we check all possible ways using 1; all ways with just 1.
        # then in the next coin loop, we check all possible ways using 2 (this adds it to the previous ways with just 1); all ways with just 1 AND 2
        # last coin loop, we check all possible ways using 5 (this adds to the previous ways with just 1 AND 2); all ways with just 1 AND 2 AND 5

        for c in coins:
            for i in range(1, amount + 1):
                dp[i] += (dp[i - c] if i-c >= 0 else 0) 
        
        return dp[-1]
        