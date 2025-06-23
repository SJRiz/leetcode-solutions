# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If the lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Store the count of each character in a hashmap because O(1) lookup
        s_counter = {}
        t_counter = {}

        # Count characters in s string
        for char in s:
            if char in s_counter:
                s_counter[char] += 1
            else:
                s_counter[char] = 1
        
        # Count characters in t string
        for char in t:
            if char in t_counter:
                t_counter[char] += 1
            else:
                t_counter[char] = 1

        # Return true or false depending if they are equal
        return s_counter == t_counter