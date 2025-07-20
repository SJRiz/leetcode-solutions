"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:     # Base case (starts True), send it to the upper node
            return True

        elif p and q and p.val == q.val:    # Check to see if left and right nodes are the same
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
            
        else:
            return False
        
    # Solution is O(n) time and O(n) space