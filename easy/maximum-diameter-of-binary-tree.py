"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.highest = 0

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.highest = max(self.highest, left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.highest
    
    # Solution is O(n) time and O(h) space