from typing import List
from collections import defaultdict

"""
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # this is basically just counting how many seperate trees there are
        # you just dfs with a seen set

        seen = set()
        cnt = 0

        nodes = defaultdict(list)

        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)

        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for n in nodes[node]:
                dfs(n)

        for i in range(n):
            if i not in seen:
                cnt += 1
                dfs(i)
        
        return cnt
    
    # Solution is O(V + E) time and O(V) space
