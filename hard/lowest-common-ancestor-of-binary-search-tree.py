"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root):
            # Went too far
            if not root:
                return

            # If both are less than the current node, then the next ancestor is somewhere on the left
            if p.val < root.val and q.val < root.val:
                lca = search(root.left)

            # Likewise if its larger
            elif p.val > root.val and q.val > root.val:
                lca = search(root.right)

            # If p and q are larger/smaller, or if the current node is the same value as any of those, we found a split
            else:
                return root
            
            return lca
        
        return search(root)
    
    # Solution is O(h) time and O(h) space. Can be improved by doing an iterative approach rather than recursion