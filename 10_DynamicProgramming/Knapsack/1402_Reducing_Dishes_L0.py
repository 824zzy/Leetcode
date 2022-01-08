""" https://leetcode.com/problems/reducing-dishes/
choose dish: (i+1-dis)*A[i]+dfs(i+1, dis)
discard dish: dfs(i+1, dis+1)
"""
class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        A.sort()
        
        @cache
        def dfs(i, dis):
            if i==len(A): return 0
            # choose
            c = (i+1-dis)*A[i]+dfs(i+1, dis)
            # discard
            d = dfs(i+1, dis+1)
            return max(c, d)
        
        return dfs(0, 0)
