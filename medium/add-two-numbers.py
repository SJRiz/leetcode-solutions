# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = res = ListNode()
        curr1 = l1
        curr2 = l2

        carry = 0

        # First, loop through both lists
        while curr1 and curr2:
            value = curr1.val + curr2.val + carry
            dummy.val = (value) % 10
            carry = (value) // 10

            curr1 = curr1.next
            curr2 = curr2.next
            
            if curr1 or curr2:
                dummy.next = ListNode()
                dummy = dummy.next

        # Then, loop through the longer list
        curr3 = curr1 if curr1 else curr2
        while curr3:
            value = curr3.val + carry
            dummy.val = (value) % 10
            carry = (value) // 10

            curr3 = curr3.next

            if curr3:
                dummy.next = ListNode()
                dummy = dummy.next
        
        # Finally, add any leftover carries
        if carry > 0:
            dummy.next = ListNode()
            dummy = dummy.next
            dummy.val += carry

        return res
    
    # Solution is O(n) time and O(1) extra space. I will redo this question later for more clarity