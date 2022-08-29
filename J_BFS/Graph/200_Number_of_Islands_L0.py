""" https://leetcode.com/problems/number-of-islands/submissions/
count island by bfs
"""
from header import *

class Solution:
    def numIslands(self, A: List[List[str]]) -> int:
        m, n = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(x, y):
            Q = [(x, y)]
            A[x][y] = '0'
            while Q:
                x, y = Q.pop(0)
                for dx, dy in D:
                    if 0<=x+dx<m and 0<=y+dy<n and A[x+dx][y+dy]=='1':
                        A[x+dx][y+dy] = '0'
                        Q.append((x+dx, y+dy))
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if A[i][j]=='1':
                    bfs(i, j)
                    ans += 1
        return ans