# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Use fast and slow pointers to find the middle node.
        fp = head
        middle = head
        while fp and fp.next:
            fp = fp.next.next
            middle = middle.next

        # Once we find the middle, disconnect the first half from the second half
        prev = None
        curr = middle.next
        middle.next = None

        # Reverse the second half
        while curr:
            curr2 = curr.next
            curr.next = prev

            prev = curr
            curr = curr2

        # We will now use a two pointer like approach. We will connect the left-most node to the right-most, and increment to the next left/right
        p1 = head
        p2 = prev
        while p1 and p2:
            left = p1.next
            right = p2.next

            p1.next = p2
            p1 = left
            p2.next = p1
            p2 = right
            
    # Solution is O(n) time and O(1) space complexity