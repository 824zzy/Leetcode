""" https://leetcode.com/problems/minimum-path-cost-in-a-grid/
Maze DP

Time complexity: O(m*n*n)
"""
class Solution:
    def minPathCost(self, A: List[List[int]], moveCost: List[List[int]]) -> int:
        mp = {}
        for i in range(len(moveCost)): mp[i] = moveCost[i]
            
        @cache
        def dp(i, j):
            if i==len(A)-1: return A[i][j]
            ans = inf
            for jj in range(len(A[0])):
                ans = min(ans, A[i][j]+mp[A[i][j]][jj]+dp(i+1, jj))
            return ans
        
        return min(dp(0, j) for j in range(len(A[0])))