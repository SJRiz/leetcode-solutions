"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.
"""

from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # dfs (similar to traversing a binary tree) while keeping track of visited stack
        # a level-order traversal
        # apparently this is a topological sort

        courses = defaultdict(list)
        visiting = set()
        visited = set()
        course_stack = []

        for curr, prereq in prerequisites:
            courses[curr].append(prereq)        # {0: [1, 2], 1: [2]}

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            visited.add(course)

            for prereq in courses[course]:
                res = dfs(prereq)
                if not res:
                    return False
            course_stack.append(course)
            visiting.remove(course)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                res = dfs(i)
                if not res:
                    return []
        
        return course_stack
    
    # Solution is O(V + E) time and space
