"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hashmap = {val: idx for idx,val in enumerate(inorder)}
        self.prev = 0

        def dfs(l, r):
            if l > r:
                return None

            node = TreeNode(val=preorder[self.prev])
            mid = hashmap[preorder[self.prev]]
            self.prev += 1

            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)

            return node

        return dfs(0, len(preorder)-1)
    
    # Solution is O(n) time and space.