# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # First, count the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Handle edge case
        if length == n:
            return head.next

        # Remove the nth node at the end (calculated by length - i)
        # Keep track of previous so when we remove the node, we connect its previous to its next
        curr = head
        prev = head
        i = 0
        while length - i != n:
            i += 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        curr.next = None

        return head