# You are given the head of a singly linked list head and a positive integer k.
# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on.
# If there are fewer than k nodes left, leave the nodes as they are.
# Return the modified list after reversing the nodes in each group of k.
# You are only allowed to modify the nodes' next pointers, not the values of the nodes.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        res = first = ListNode()
        curr = head
        while curr:
            # look k nodes ahead
            check = curr
            for _ in range(k-1):
                check = check.next if check else None
                
            if not check:
                # if there arent k nodes, then just attach the last head to the beginning
                first.next = curr
                break
            
            # reverse k nodes
            prev = None
            tail = curr
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # attack the last head (which would now be the tail) to the next head (which would also be a tail)
            first.next = prev
            first = tail
        
        return res.next
    
    # Solution is O(n) time complexity