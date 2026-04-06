# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
# You may assume that the correct output is always unique.

from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # open window till we get all characters in t
        # once we do, close the window until we dont
        # repeat until we reach end, also always constantly update minimum

        res = None
        l, r = 0, 0
        hm = defaultdict(int)
        match = Counter(t)
        count = 0   # counts number of matched characters

        while r < len(s):
            current_char = s[r]

            if current_char in t:
                hm[current_char] += 1

                if hm[current_char] == match[current_char]:
                    count += 1

                # Start closing window when we have all matches
                while count >= len(match):
                    if not res or r-l+1 <= res[1]-res[0]+1:
                        res = (l, r)

                    removing_char = s[l]

                    # decrement the count if we stopped a match
                    if removing_char in t:
                        if hm[removing_char] == match[removing_char]:
                            count -= 1
                        hm[removing_char] = max(0, hm[removing_char]-1)

                    l += 1
            r += 1
        
        return "" if not res else s[res[0]:(res[1]+1)]

    # Solution is O(n) time and constant space O(52)