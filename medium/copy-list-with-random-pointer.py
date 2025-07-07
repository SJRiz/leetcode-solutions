# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.
# Create a deep copy of the list.
# The deep copy should consist of exactly n new nodes, each including:
    # The original value val of the copied node
    # A next pointer to the new node corresponding to the next pointer of the original node
    # A random pointer to the new node corresponding to the random pointer of the original node

# Note: None of the pointers in the new list should point to nodes in the original list.
# Return the head of the copied linked list.

from collections import defaultdict

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # We will use a hashmap and store the old nodes as keys, and the new nodes as their values. This also allows us to easily lookup the next and random node, as they will point to the key in the hashmap.
        # If we haven't accessed that node yet, we will put a node their with 0 as a placeholder (the value will be corrected once the loop reaches that node)
        # Also create a "None" key for any null values
        hashmap = defaultdict(lambda: Node(0))
        hashmap[None] = None
        curr = head
        
        while curr:
            hashmap[curr].val = curr.val
            hashmap[curr].next = hashmap[curr.next]
            hashmap[curr].random = hashmap[curr.random]
            curr = curr.next
        
        return hashmap[head]
    
    # Solution is O(n) time and O(n) space complexity