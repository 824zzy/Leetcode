""" https://leetcode.com/problems/course-schedule-iv/
use floyd-warshall to find connected direct points
"""
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dist = [[inf for _ in range(n)] for _ in range(n)]
        for i in range(n): dist[i][i] = 0
        for i, j in prerequisites:
            dist[i][j] = 1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])      
        
        return [1 if dist[i][j]!=inf else 0 for i, j in queries]