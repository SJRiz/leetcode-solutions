# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # Initial search: Check k=1 while simultaneously finding the highest
        highest = 0
        lowest = 1
        ate = 0

        for pile in piles:
            highest = max(highest, pile)
            ate += pile
        
        if ate <= h:
            return lowest

        # Use binary search to find the ideal k (if it overshoots h then go right, otherwise go left)
        res = highest
        while lowest <= highest:
            m = (lowest + highest) // 2
            ate = 0
            for pile in piles:
                ate += math.ceil(float(pile) / m)

                # If we took too much time, increase the rate. Also end the for-loop early
                if ate > h:
                    lowest = m + 1
                    break
            
            # If we took less time, nudge forward (keep track of the previous lowest just incase the next iteration overshoots)
            if ate <= h:
                res = m
                highest = m - 1
        
        return res
    
    # Solution is O(nlog(m)) time and O(1) space