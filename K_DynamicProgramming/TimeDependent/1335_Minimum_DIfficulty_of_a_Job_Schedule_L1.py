""" https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
dfs(i, d) = min(max(A[i:j]) + dfs(j, d-1)), j = i+1, ...
"""
class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        if d>len(A): return -1
        
        @cache
        def dfs(i, k):
            if k==1: return max(A[i:])
            return min([max(A[i:j])+dfs(j, k-1) for j in range(i+1, len(A))], default=inf)
        
        return dfs(0, d)