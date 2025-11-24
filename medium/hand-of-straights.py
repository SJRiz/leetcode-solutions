from typing import List
from collections import Counter

"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        things = Counter(hand)

        for key in things:
            while things[key] > 0:
                for i in range(groupSize):
                    if key + i in things and things[key+i] > 0:
                        things[key+i] -= 1
                    else:
                        return False
        
        return True
