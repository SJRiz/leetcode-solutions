from typing import List

"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            if not carry:
                break
            rem = (digits[i] + carry)%10
            carry = (digits[i] + carry)//10
            digits[i] = rem
        
        if carry:
            digits.insert(0, carry)

        return digits

    # solution is O(n) time and O(1) space