from typing import List

"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # so u gotta find the first and last time a letter appears
        # this is just a merge interval problem lol
        
        intervals = {}
        res = []

        # create intervals
        for i in range(len(s)):
            if s[i] in intervals:
                intervals[s[i]][1] = i
            else:
                intervals[s[i]] = [i,i]
        
        # merge
        prev = None
        for x in intervals:
            start, end = intervals[x][0], intervals[x][1]
            if not prev:
                prev = [start, end]
                continue
            
            if start < prev[1]:
                prev[1] = max(prev[1], end)
            else:
                res.append(prev[1]-prev[0]+1)
                prev[0] = start
                prev[1] = end

        res.append(prev[1]-prev[0]+1)
        return res


            