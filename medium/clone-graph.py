"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # do a bfs/dfs with a visited set
        if not node:
            return None

        seen = {}
        seen[node] = Node(node.val)
        stack = [node]

        while stack:
            top = stack.pop()
            if top:
                for neighbor in top.neighbors:
                    if neighbor not in seen:
                        seen[neighbor] = Node(neighbor.val)
                        stack.append(neighbor)
                    seen[top].neighbors.append(seen[neighbor])
        
        return seen[node]