"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # caabbc
        # We either take the current 'split' and move left pointer all the way to right pointer, or just increment the right pointer
        # Base cases: pointer out of bounds, current string is not valid, and is valid

        res = []
        sol = []

        def valid(s):
            return s == s[::-1]

        def backtrack(left, right, num):
            if sol and not valid(sol[-1]):
                return
            if right == len(s)+1 or left == len(s):
                if num == len(s):
                    res.append(sol[:])
                return
            
            backtrack(left, right+1, num)

            sol.append(s[left:right])
            backtrack(right, right+1, num + right-left)
            sol.pop()
        
        backtrack(0,1,0)
        return res
    
    # Solution is O(n*2^n) time and O(n) space
