# Given the root of a binary tree, invert the tree, and return its root.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        deq = deque()
        deq.append(root)

        while deq:
            node = deq.popleft()
            if node:
                deq.append(node.left)
                deq.append(node.right)
                node.left, node.right = node.right, node.left
        
        return root
    
    # Solution is O(n) time and O(n) space