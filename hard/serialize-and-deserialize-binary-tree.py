"""
Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Just use bfs on both functions lol and use : as a delimiter and use n for none
class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "n"

        deq = deque([root])
        s = str(root.val) + ':'
        while deq:
            for _ in range(len(deq)):
                node = deq.popleft()
                if node:
                    deq.append(node.left)
                    deq.append(node.right)
                    s += (str(node.left.val) if node.left else 'n') + ':'
                    s += (str(node.right.val) if node.right else 'n') + ':'
        
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(":")
        if vals[0] == "n":
            return None
        
        root = TreeNode(vals[0])
        deq = deque([root])
        idx = 1

        while deq:
            node = deq.popleft()

            if vals[idx] != "n":
                left_node = TreeNode(vals[idx])
                node.left = left_node
                deq.append(left_node)
            idx += 1

            if vals[idx] != "n":
                right_node = TreeNode(vals[idx])
                node.right = right_node
                deq.append(right_node)
            idx += 1
        
        return root
    
    # Solution is O(n) time and O(n) space for both functions
        


