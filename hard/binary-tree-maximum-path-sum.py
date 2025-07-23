"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Track highest sum on left subtree and right subtree
        # If the current node val is bigger than the node val + previous, switch to that
        # For the highest, track all possible path combinations and get the highest of them

        highest = float("-inf")

        def dfs(node):
            nonlocal highest

            if not node:
                return 0

            highest_left = dfs(node.left)
            highest_right = dfs(node.right)
            
            # These are all the possible ways to calculate the path sums (if neither are bigger than the current highest then ignore it)
            highest = max(
                node.val,
                node.val + highest_left + highest_right,
                node.val + highest_left,
                node.val + highest_right,
                highest
            )

            return max(node.val, node.val + highest_left, node.val + highest_right)
        
        dfs(root)
        return highest
    
    # Solution is O(n) time and O(h) space. Another way to approach this problem is to ignore negative path sums entirely