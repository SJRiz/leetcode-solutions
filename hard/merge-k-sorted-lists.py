"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""

import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a heap to track the smallest nodes first at the beginning of the list
        # (the count is used as a unique identifier, prevents errors with comparing ListNode objects)
        count = 0
        minHeap = []
        for x in lists:
            count += 1
            if x:
                minHeap.append((x.val, count, x))

        heapq.heapify(minHeap)
        dummy = ListNode()
        curr = dummy

        # Constantly pop the smallest element in the heap, and then add that node's next value in the heap
        # This smallest element will be the next in the linked list
        # Repeat until there are no more elements
        while minHeap:
            count += 1
            smallest = heapq.heappop(minHeap)
            if smallest[2].next:
                heapq.heappush(minHeap, (smallest[2].next.val, count, smallest[2].next))

            curr.next = smallest[2]
            curr = curr.next
        
        return dummy.next
    
    # Solution is O(nlog(k)) time and O(k) space
