"""
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.
"""

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        # Do a bfs
        deq = deque([root])
        i = 1
        res = []

        if not root:
            return res

        while deq:
            curr = []
            # loop through the current level
            for _ in range(i):
                node = deq.popleft()
                if node:
                    deq.append(node.left)
                    deq.append(node.right)
                    curr.append(node.val)  
            if curr:
                res.append(curr)

            # Next level will start at the current length of the deque
            i = len(deq)
        
        return res
    
    # Solution is O(n) time and O(w) extra space