# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Track the index of last-seen characters
        seen = {}
        longest = 0

        # We will use a dynamic sliding window to solve this
        i = 0
        for j in range(len(s)):

            # If the character has already been seen, then move 1 ahead to the index we last saw the character
            if s[j] in seen and seen[s[j]] >= i:
                i = seen[s[j]] + 1
            
            # Record the index we track any character
            seen[s[j]] = j

            # j-i+1 gives the current length of the substring
            longest = max(j - i + 1, longest)

        return longest
    
    # Solution is O(n) time and O(m) space complexity, where m is the number of unique characters

