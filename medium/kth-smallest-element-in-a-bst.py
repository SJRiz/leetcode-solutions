"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = k
        kth = None

        def dfs(node):
            nonlocal count, kth
            if not node or kth:
                return
            dfs(node.left)
            count -= 1
            if count == 0:
                kth = node.val
            dfs(node.right)
            
        dfs(root)
        return kth
    
    # Solution is O(n) time and O(n) space.