""" https://leetcode.com/problems/cherry-pickup-ii/
Define dfs(i, j1, j2) to represent the amout of cherries when the two robots are at (i, j) and (i, jj) respectively. 
"""
class Solution:
    def cherryPickup(self, A: List[List[int]]) -> int:
        @cache
        def dfs(i, j1, j2):
            if not (0<=j1<=j2<len(A[0])): return -inf
            if i==len(A): return 0
            ans = A[i][j1]+(j1!=j2)*A[i][j2]
            return ans+max(dfs(i+1, jj1, jj2) for jj1 in (j1-1, j1, j1+1) for jj2 in (j2-1, j2, j2+1))
        
        return dfs(0, 0, len(A[0])-1)