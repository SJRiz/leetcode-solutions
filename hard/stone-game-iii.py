class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # we start backwards and build from there
        # suppose dfs(6) = 7. this mean whoever lands on index 6, the best score they can achieve on that index is 7.
        # how is this calculated? dfs(6) = max of (taking this, or this + next, or this + next + next subtracted by dfs(next index))
        dp = {}

        def dfs(i):
            if i >= len(stoneValue):
                # base case
                return 0

            # note that opponent optimal also has current player's score, so res is just calculating the new score by adding the new taken
            res = float("-inf")
            for next in [1, 2, 3]:
                if i+next not in dp:
                    dp[i+next] = dfs(i+next)
                opponent_optimal = dp[i+next]
                res = max(res, sum(stoneValue[i:i+next]) - opponent_optimal)
            return res
        
        ans = dfs(0)
        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        else:
            return "Tie"