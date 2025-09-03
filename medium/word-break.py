from functools import lru_cache
from typing import List

"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = False

        def wordmatch(start, word):
            for i in range(len(word)):
                if start+i >= len(s) or s[start+i] != word[i]:
                    return False
            return True

        @lru_cache
        def dp(start):
            nonlocal res
            if res or start > len(s):
                return
            if start == len(s):
                res = True
                return
            for word in wordDict:
                if wordmatch(start, word):
                    dp(start + len(word))

        dp(0)
        
        return res
    
    # Solution is O(n * m * L) time and O(n) space where m is the number of words, n is the length of string s, and t is the max length of a worddict