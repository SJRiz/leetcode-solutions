from functools import lru_cache

"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # its just a dfs where u keep track of both indexes
        path = []

        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(None)
        def dfs(idx1, idx2):
            if path and path[-1] != s3[idx1+idx2-1]:
                return False
            elif idx1 == len(s1) and idx2 == len(s2):
                return "".join(path) == s3[:idx1 + idx2]
            
            left = False
            right = False

            if idx1 < len(s1):
                path.append(s1[idx1])
                left = dfs(idx1+1, idx2)
                path.pop()

            if idx2 < len(s2):
                path.append(s2[idx2])
                right = dfs(idx1, idx2+1)
                path.pop()
            return left or right
        
        return dfs(0,0)
            