from typing import List

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # topological sort with seen set
        visiting = set()

        # make tree
        nodes = {i:[] for i in range(n)}
        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)

        def dfs(node, parent):
            if node in visiting:
                return False

            visiting.add(node)
            
            for n in nodes[node]:
                if n != parent and dfs(n, node) == False:
                    return False
            return True

        return dfs(0, None) and len(visiting) == n
    
    # Solution is O(V + E) time and O(V) space
