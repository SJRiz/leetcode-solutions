"""
You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.
"""

from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        # We can do a greedy approach to solve this problem
        # If one index goes out of bounds, end the function early
        players.sort()
        trainers.sort()
        p, t = 0, 0
        res = 0
        
        while t < len(trainers) and p < len(players):
            
            # If the current index player level is too high, move the trainer index until it meets the condition
            while players[p] > trainers[t]:
                t += 1
                if t > len(trainers)-1:
                    return res

            # Every loop will always result in +1 to the output value
            res += 1   
            p+=1
            t+=1
        
        return res
    
    # Solution is O(nlog(n)) time