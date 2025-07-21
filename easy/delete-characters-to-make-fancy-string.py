"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        curr = None 
        count = 0
        res = ''

        for c in s:
            if not curr or c != curr:
                curr = c
                count = 1
            else:
                count += 1
            
            if count < 3:
                res += c
        
        return res
    
    # Solution is O(n) time and O(1) extra space