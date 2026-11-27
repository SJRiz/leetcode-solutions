# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # u could use that one euclid algo but i forgot how to do it
        def gcd(x,y):
            if x >= y:
                larger, smaller = x, y
            else:
                larger, smaller = y, x

            for i in range(smaller, -1, -1):
                if larger % i == 0 and smaller % i == 0:
                    return i
        
        dummy = head
        curr = dummy
        while curr:
            if curr.next:
                nxt = curr.next
                new = ListNode(val=gcd(curr.val, nxt.val), next=nxt)
                curr.next = new
                curr = curr.next.next
            else:
                return dummy
            