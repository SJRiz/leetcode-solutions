# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = -1
        res = 0
        curr = head

        # This solution rearranges the general formula for binary numbers by factoring out n, where n is the number of bits
        #  e.g. 1*2^(n) + 0*2^(n-1) + 1*2^(n-2) + ... + 1*2^1 + 1*2^0
        # = 2^n(1*2 + 0*2^-1 + 1*2^-2 + ... + 1*2^(1-n) + 1*2^(-n))
        while curr:
            n += 1
            res += 2**(-1 * n) * curr.val
            curr = curr.next
        
        return int(res * 2**(n))
    
    # Solution is O(n) time and O(1) space.