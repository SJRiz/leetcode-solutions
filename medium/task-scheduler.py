"""
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.
"""

from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [count[c]*-1 for c in count]
        heapq.heapify(maxHeap)

        deq = deque()
        time = 0

        while maxHeap or deq:
            time += 1

            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq + 1 < 0:
                    deq.append((freq+1, time+n))

            if deq and deq[0][1] <= time:
                new_freq = deq.popleft()[0]
                heapq.heappush(maxHeap, new_freq)
        
        return time
    
    # Solution is O(nlog(k)) and O(k) space where k is the number of unique characters (in this case, the max would be k = 26)