""" https://leetcode.com/problems/number-of-closed-islands/
opposite 1020
"""
class Solution:
    def closedIsland(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(x, y):
            if not (0<=x<len(A) and 0<=y<len(A[0])): return False
            elif A[x][y]==1: return True
            A[x][y] = 1
            ans = True
            for dx, dy in D:
                ans &= dfs(x+dx, y+dy)
            return ans
        
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if not(not i or not j or i==len(A)-1 or j==len(A[0])-1) and A[i][j]==0:
                    if dfs(i, j): ans += 1
        return ans