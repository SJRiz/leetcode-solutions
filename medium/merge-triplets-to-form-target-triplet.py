from typing import List

"""
A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
"""

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # just ignore the triplets that break the target border
        # if its within the border then take the max between the triplet and current max
        # borderline personality disorder algorithm

        res = [0,0,0]

        for t1, t2, t3 in triplets:
            if t1 <= target[0] and t2 <= target[1] and t3 <= target[2]:
                res = [max(t1, res[0]), max(t2, res[1]), max(t3, res[2])]
        
        return (res[0] == target[0] and res[1] == target[1] and res[2] == target[2])