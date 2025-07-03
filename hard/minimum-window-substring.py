# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
# You may assume that the correct output is always unique.

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Strategy: use two pointers (sliding window)
        # Continuosly move the right pointer until the window becomes valid
        # If the window is valid, shrink it until it is invalid
        # This approach ensures we get the smallest subtring that starts with a char from t, and contains the rest from t
        # We save the smallest index as a tuple, and track the matched counters by using need and have variables

        t_count = defaultdict(int)
        window_count = defaultdict(int)

        for c in t:
            t_count[c] += 1

        have = len(t_count)
        need = 0

        smallest_index = None

        left = 0
        for right in range(len(s)):
            window_count[s[right]] += 1

            # If we have a matching char, and their counts are the same, thats +1 need
            if s[right] in t_count and window_count[s[right]] == t_count[s[right]]:
                need += 1

            # If we have all chars matching, shrink until not matching
            while need == have:

                # Make sure to check if the smallest index ever changes (distance between left and right decides this)
                if not smallest_index or right - left + 1 < smallest_index[1] - smallest_index[0] + 1:
                    smallest_index = (left, right)
                
                # When moving the left pointer, we subtract from the counter.
                # If a character no longer matches, then thats -1 need
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    need -= 1
                if window_count[s[left]] < 1:
                    del window_count[s[left]]
                left += 1

        return "" if not smallest_index else s[smallest_index[0]:smallest_index[1]+1] 

    # Solution is O(n) time and constant space O(52)