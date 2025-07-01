# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # We will use two pointers, left and right
        left = 0
        right = len(s) - 1

        while left < right:

            # Move the pointers until they are both on a proper alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # If the pointers are ever not equal, then that means its not valid
            if s[left].lower() != s[right].lower():
                return False

            # Move to the next iteration
            left += 1
            right -= 1

        # If it never returns False, then it must be valid.
        return True
    
    # Solution is O(n) time.