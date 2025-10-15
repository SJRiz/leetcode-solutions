from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        cache = {}  # (i, can_buy)
        # dfs with 2 states; day and canBuy
        # if canBuy = true, you can either wait or buy
        # if canBuy = false, you can either wait or sell now (then you'd index + 2)

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0
            if (i, can_buy) in cache:
                return cache[(i, can_buy)]

            if can_buy == True:
                cache[(i, can_buy)] = max(dfs(i + 1, can_buy), dfs(i + 1, not can_buy) - prices[i])
                return cache[(i, can_buy)]
            else:
                # sell
                cache[(i, can_buy)] = max(dfs(i + 1, can_buy), dfs(i + 2, not can_buy) + prices[i])
                return cache[(i, can_buy)]
        
        return dfs(0, True)
    
    # Solution is O(n) time and space