"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # insert -> index word2
        # delete -> index word1
        # replace -> index both
        # same character -> index both but dont add anything_

        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

        # base cases:
        for r in range(len(word1) + 1):
            dp[r][0] = r
        for c in range(len(word2) + 1):
            dp[0][c] = c

        for r in range(1, len(word1)+1):
            for c in range(1, len(word2)+1):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])

        return dp[-1][-1]
