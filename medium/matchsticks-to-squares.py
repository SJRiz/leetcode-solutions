"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.
"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # add up all lengths, divide by 4
        # if not integer we already know and can return false
        # otherwise the problem is just finding how to make the array evenly split 4 ways
        # backtrack

        # target = 16, matchsticks = [4,4,3,2,2,1]

        matchsticks.sort(reverse=True)
        target = sum(matchsticks)

        if target%4 != 0:
            return False

        side = target/4

        for match in matchsticks:
            if match > side:
                return False

        path = {}

        def dfs(count, path, idx):
            if count > side:
                return False
            if count == side:
                count = 0
                idx = 0
            if len(path) == len(matchsticks):
                return True
            
            prev = None

            for i in range(idx, len(matchsticks)):
                if i in path:
                    continue
                if matchsticks[i] != prev:
                    prev = matchsticks[i]
                    path[i] = matchsticks[i]
                    if dfs(count+matchsticks[i], path, i) == True:
                       return True
                    path.pop(i)

            return False

        return dfs(0, path, 0)


