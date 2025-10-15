"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # do a dfs, but keep track of nodes you are visiting and already visited
        # if you come across a node that you are already visiting in the recursion stack, bad

        courses = defaultdict(list)
        visiting = set()

        for curr, prereq in prerequisites:
            courses[curr].append(prereq)
        
        def dfs(course):    # takes a course number (1, 2, 3) and then dfs the indexes
            if course not in courses:
                return True     # that course has no prereqs so good
            if course in visiting:
                return False
            
            visiting.add(course)
            for prereq in courses[course]:
                res = dfs(prereq)
                if res == False:
                    return False
            visiting.remove(course)
            courses[course] = []
            
            return True
            
        for i in range(numCourses):
            res = dfs(i)
            if not res:
                return False
        
        return True
    
    # Solution is O(V + E) time and space where V is the number of nodes and E is the number of edges/connections