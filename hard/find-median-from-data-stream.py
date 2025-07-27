"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

import heapq

class MedianFinder:
    # Lets try using a minheap and a maxheap
    # the maxheap will store values less than or equal to the median (first half of list)
    # the minheap will store values greater than or equal to the median (second half of list)
    # if the added number is smaller than or equal to the maxheap, add it to the maxheap. Otherwise add to minheap
    # restore balance on both heaps until the lengths differ by no more than 1

    def __init__(self):
        self.maxHeap = [float('inf')]
        self.minHeap = [float('inf')]

    def addNum(self, num: int) -> None:
        if num <= self.maxHeap[0]*-1:
            heapq.heappush(self.maxHeap, num*-1)
        else:
            heapq.heappush(self.minHeap, num)
        
        while len(self.maxHeap) - 1 > len(self.minHeap):
            new_num = heapq.heappop(self.maxHeap)*-1
            heapq.heappush(self.minHeap, new_num)

        while len(self.minHeap) - 1 > len(self.maxHeap):
            new_num = heapq.heappop(self.minHeap)*-1
            heapq.heappush(self.maxHeap, new_num)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0]*-1) / 2
        return self.maxHeap[0]*-1 if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]
    
    # Solution is O(log(n)) time for every addnum call, and O(n) space
        