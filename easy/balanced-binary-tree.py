"""
Given a binary tree, determine if it is height-balanced.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.diff = 0

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.diff = max(self.diff, abs(left - right))
            return 1 + max(left, right)

        dfs(root)
        return True if self.diff < 2 else False
    
    # Solution is O(n) time and O(h) space