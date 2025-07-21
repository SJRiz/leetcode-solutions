"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        # iterate through a dfs and keep track of the biggest value through previous
        def dfs(root, biggest):
            if not root:
                return
            if biggest is None or root.val >= biggest:
                biggest = root.val
                self.res += 1

            dfs(root.left, biggest)
            dfs(root.right, biggest)

        dfs(root, None)
        return self.res
    
    # Solution is O(n) time and O(h) space

        