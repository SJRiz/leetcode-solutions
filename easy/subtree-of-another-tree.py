"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:   
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # DFS to check if a tree is equal
        def dfs(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return (dfs(p.left, q.left) and dfs(p.right, q.right))
            else:
                return False

        # BFS till we find a candidate, then DFS
        deq = deque([root])
        while deq:
            node = deq.popleft()
            if node:
                deq.append(node.left)
                deq.append(node.right)
                if node.val == subRoot.val and dfs(node, subRoot):
                    return True
        
        return False
    
    # Solution is O(n * m) time and O(n + m) space