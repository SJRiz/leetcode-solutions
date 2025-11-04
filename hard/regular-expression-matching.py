class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # "." means any char, "x*" means 0 or more of x
        # we note that .* means 0 or more of ., and this can be used to easily match

        # let i be the row (p) and j be the col (s)
        # if i is a dot, then (i,j) is true if (i-1, j-1) is true
        # if i is a char, same logic as a above AND if p[i] == s[j]
        # if i is * , then (i,j) will be true if either (i-1, j) is true, or if (i, j-1) is true and p[i] == s[j].

        dp = [[False]*(len(s)+1) for _ in range(len(p) + 1)]

        # do base cases
        dp[0][0] = True
        for i in range(1, len(dp)):
            if p[i-1] == "*":
                dp[i][0] = dp[i-2][0]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[i-1] != "*":
                    dp[i][j] = dp[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == ".")
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-2][j] or (dp[i][j-1] and (p[i-2] == s[j-1] or p[i-2] == "."))


        return dp[-1][-1]


