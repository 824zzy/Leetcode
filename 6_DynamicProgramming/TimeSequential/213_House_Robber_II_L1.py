""" https://leetcode.com/problems/house-robber-ii/submissions/
two pass: A[1:], A[:-1]
"""
class Solution:
    def rob(self, A: List[int]) -> int:
        @lru_cache(None)
        def dfs1(i):
            if i<1: return 0
            return max(dfs1(i-1), A[i]+dfs1(i-2))
        
        @lru_cache(None)
        def dfs2(i):
            if i<0: return 0
            return max(dfs2(i-1), A[i]+dfs2(i-2))
        
        return max(dfs1(len(A)-1), dfs2(len(A)-2)) if len(A)>1 else A[0]
    
class Solution:
    def rob(self, A: List[int]) -> int:
        if len(A)==1: return A[0]
        elif len(A)==2: return max(A[0], A[1])
        
        dp1 = [0] * (len(A))
        dp1[0], dp1[1] = A[0], max(A[0], A[1])
        for i in range(2, len(A)-1):
            dp1[i] = max(A[i]+dp1[i-2], dp1[i-1])
            
        dp2 = [0] * (len(A))
        dp2[1], dp2[2] = A[1], max(A[1], A[2])
        for i in range(3, len(A)):
            dp2[i] = max(A[i]+dp2[i-2], dp2[i-1])
            
        return max(dp1[-2], dp2[-1])