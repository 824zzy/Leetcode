""" https://leetcode.com/problems/jump-game-iii/
"""
class Solution:
    def canReach(self, A: List[int], s: int) -> bool:
        seen = set()
        
        def dfs(i):
            if not 0<=i<len(A) or i in seen: return False
            if A[i]==0: return True
            seen.add(i)
            return dfs(i+A[i]) or dfs(i-A[i])
        
        return dfs(s)