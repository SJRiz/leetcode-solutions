"""
You are given two strings s and t, both consisting of english letters.

Return the number of distinct subsequences of s which are equal to t.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]

        for r in range(len(t)):
            cum = 0
            for c in range(len(s)):
                cum += dp[r][c]
                
                # dp[r+1][c+1] will be the running sum of the previous row, if s[r] == s[t]
                if t[r] == s[c]:
                    dp[r+1][c+1] = cum if r != 0 else 1
        
        return sum(dp[-1])