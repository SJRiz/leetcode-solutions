# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
# Both strings only contain lowercase letters.

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # We will use a window with a fixed length (length of s1)
        # Count the letters in s1, and then we will count the letters in s2 inside the window
        length = len(s1)
        s1_count = defaultdict(int)
        window_count = defaultdict(int)
        for c in s1:
            s1_count[c] += 1
        
        left = 0

        for right in range(len(s2)):
            window_count[s2[right]] += 1

            # Once the right pointer is far enough from the left, the left pointer will increment and remove counters outside the window
            if right >= length:
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:

                    # Delete the character from the hashmap if it reaches 0
                    del window_count[s2[left]]
                left += 1

            if s1_count == window_count:
                return True
        
        return False

    # Solution is O(n) time and O(1) space (s1_count and window_count max out at 26 characters)

