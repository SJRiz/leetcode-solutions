"""
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # Every node will have a left boundary and a right boundary
        # If the node value is not between this boundary then its not a valid BST
        def valid(left_b, node, right_b):
            if not node:
                return True
            if not (left_b < node.val < right_b):
                return False

            # The left node's boundary will be the same as the current node's left boundary, but the right boundary will be the current node value
            # Opposite for the right node
            return valid(left_b, node.left, node.val) and valid(node.val, node.right, right_b)
        
        return valid(float('-inf'), root, float('inf'))
    
    # Solution is O(n) time and O(n) space