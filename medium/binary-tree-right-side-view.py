"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        deq = deque([root])
        res = []

        if not root:
            return res

        # Do a bfs
        while deq:

            # The top of the deque will always be the rightmost value for every level
            res.append(deq[-1].val)

            # The level group is defined by the current length of the deque
            i = len(deq)
            for _ in range(i):
                node = deq.popleft()
                if node and node.left:
                    deq.append(node.left)
                if node and node.right:
                    deq.append(node.right)
        
        return res
    
    # Solution is O(n) time and O(w) extra space