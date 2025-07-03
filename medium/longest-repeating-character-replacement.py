# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Use a sliding window to find the substring
        # We will count the frequency of each character in the window. Keep track of the highest frequency
        count_window = defaultdict(int)
        most_freq = None
        res = 0

        left = 0
        for right in range(len(s)):
            count_window[s[right]] += 1
            if not most_freq or count_window[s[right]] > count_window[most_freq]:
                most_freq = s[right]

            # The window condition is that length - frequency <= k.
            # If we decount the numbers, we dont have to worry about changing the frequency
            # This is because the max string length is maximized by the frequency
            if right - left + 1 - count_window[most_freq] > k:
                count_window[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
    
    # Solution is O(n) time and O(m) space complexity, where m is the number of unique characters
            
                    