"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        # expand outward, this time just count
        count = 0

        for i in range(len(s)):
            # odd:
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            # even:
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count
    
    # O(n^2) time and O(1) space