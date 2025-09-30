"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        c = len(text1)+1    # cols
        r = len(text2)+1    # rows

        dp = [[0] * c for _ in range(r)]

        for j in range(1, c):
            highest = 0
            for i in range(1, r):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = max(dp[i][j-1], highest + 1)
                else:
                    dp[i][j] = dp[i][j-1]
                
                # look for previous highest
                highest = max(highest, dp[i][j-1])

        res = 0
        for i in range(r):
            res = max(res, dp[i][c-1])
        
        return res
    
    # Solution is O(n*m) time and space