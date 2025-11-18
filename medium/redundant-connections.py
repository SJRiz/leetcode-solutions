from typing import List

"""
In this problem, we are given a list of edges that form a graph which is almost a tree, except for one extra edge that creates a cycle. Our task is to find that redundant edge.
"""

class Solution:
    # The solution to this problem is using the Union-Find algorithm.
    # Union-Find uses 2 functions: find and union.
    # Find: recursively finds the root/parent of a node (via the parents array). We stop when the node is its own parent.
    # Union: connects two nodes by linking their roots/parents. If they have the same root, its a loop. Otherwise, compare ranks, and change parent of the lower rank. 

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        pars = [i for i in range(n)]
        ranks = [1] * n

        def find(node):
            res = pars[node]
            while res != pars[res]:
                pars[res] = pars[pars[res]]    # path compression
                res = pars[res]
            
            return res
        
        def union(n1, n2):
            node1, node2 = find(n1), find(n2)
            if node1 == node2:
                return [n1, n2]

            if ranks[node1] >= ranks[node2]:
                ranks[node1] += ranks[node2]
                pars[node2] = node1
            else:
                ranks[node2] += ranks[node1]
                pars[node1] = node2
            
            return None
        
        for n1, n2 in edges:
            dupe = union(n1, n2)
            if dupe:
                return dupe
            
    # Solution is O(N) time and O(N) space.
