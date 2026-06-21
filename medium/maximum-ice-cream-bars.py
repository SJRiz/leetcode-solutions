"""
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Note: The boy can buy the ice cream bars in any order.

Return the maximum number of ice cream bars the boy can buy with coins coins.

You must solve the problem by counting sort.
"""

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted = [0]*(max(costs)+1)
        spent = 0
        amount = 0


        for i in range(len(costs)):
            sorted[costs[i]] += 1
        
        for i in range(1, len(sorted)):
            for j in range(sorted[i]):
                spent += i
                if spent > coins:
                    return amount
                amount += 1
                if spent == coins:
                    return amount
        
        return amount

# O(n + m) time and O(n) space where n is max(costs) and m is len(costs)
            