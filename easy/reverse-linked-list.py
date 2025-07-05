# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        
        while curr:
            curr2 = curr.next   # Store the next value as a variable, we will make this the curr later
            curr.next = prev    # The current node will view the previous one now

            prev = curr     # Previous becomes current, and current becomes the next stored node
            curr = curr2
            
        return prev