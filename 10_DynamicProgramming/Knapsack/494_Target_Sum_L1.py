""" https://leetcode.com/problems/target-sum/
choose or not to choose
"""
class Solution:
    def findTargetSumWays(self, A: List[int], T: int) -> int:
        @lru_cache(None)
        def dfs(i, t):
            if i==len(A): return t==0
            return dfs(i+1, t-A[i])+dfs(i+1, t+A[i])
        return dfs(0, T)
            