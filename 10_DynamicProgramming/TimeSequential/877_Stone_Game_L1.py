""" https://leetcode.com/problems/stone-game/
take gain with minus sign, so we have options P[i] - dp(i+1, j) and P[j] - dp(i, j-1)
"""
class Solution:
    def stoneGame(self, A: List[int]) -> bool:
        @cache
        def dfs(i, j):
            if i>j: return 0
            return max(A[i]-dfs(i+1, j), A[j]-dfs(i, j-1))
        return dfs(0, len(A)-1)>0