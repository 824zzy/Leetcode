""" https://leetcode.com/problems/number-of-enclaves/
1. start from edge cells and go inwards by dfs and label them as 0
2. find the remained 1's cells
"""
from header import *

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(x, y):
            if not (0<=x<len(A) and 0<=y<len(A[0])) or A[x][y]==0: return
            A[x][y] = 0
            for dx, dy in D:
                dfs(x+dx, y+dy)
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if not i or not j or i==len(A)-1 or j==len(A[0])-1:
                    dfs(i, j)
        
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==1: ans += 1
        return ans