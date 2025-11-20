"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

class Solution:
    # this is a linked list problem in disguise 
    # you can use floyd's cycle detection algorithm (fast and slower pointers) as well

    def isHappy(self, n: int) -> bool:
        seen = set()

        def square_digits(num):
            num = str(num)
            res = 0
            for c in num:
                res += int(c)*int(c)
            
            if res in seen:
                return False
            if res == 1:
                return True
            else:
                seen.add(res)
                return square_digits(res)
        
        return square_digits(n)

            
        