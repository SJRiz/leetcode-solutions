from typing import List

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # for each bracket, we can choose to either close it or not close it
        # we start with (, we either close it () or put another (( repeat 
        res = []

        def dfs(path, i):
            if not (0 <= i <= n) or len(path) > n*2:
                return
            if i == 0 and len(path) == n*2:
                res.append(path)
                return
        
            # close
            dfs(path + ")", i-1)

            # open another
            dfs(path + "(", i+1)
        
        dfs("", 0)

        return res