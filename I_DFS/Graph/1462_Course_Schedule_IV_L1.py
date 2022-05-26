""" https://leetcode.com/problems/course-schedule-iv/
1. build graph in dictionary format
2. search if any path from i-th to j-th node exists

DONT FORGET TO USE CACHE
"""
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        G = defaultdict(list)
        for i, j in prerequisites:
            G[i].append(j)
        
        @cache
        def dfs(i, end):
            if i==end: return True
            elif i not in G: return False
            
            ans = False
            for j in G[i]:
                ans |= dfs(j, end)
            return ans
                
        return [dfs(i, j) for i, j in queries]
            