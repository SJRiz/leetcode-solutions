# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Hashmaps are ideal for O(1) lookup. We can use a string's character count as the key, and make a list of values with the same "key"
        hashmap = {}

        for string in strs:

            # First, count all the characters in each string
            counter = {}
            for char in string:
                if char in counter:
                    counter[char] += 1
                else:
                    counter[char] = 1

            # We will make the character count a frozenset, so it can be hashable (also order of the character doesn't matter) and used as a key
            key = frozenset(counter.items())
            
            # If that character count sequence already exists, then add it to the list with that key
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]

        # Turn the values of the hashmap into a list
        return list(hashmap.values())

# This solution is O(n * k). It is also very slightly less optimal, as building a frozenset is quite expensive compared to making a 26 char tuple as a key.
# Nonetheless I thought my approach was very clever, and it was an acceptable solution.