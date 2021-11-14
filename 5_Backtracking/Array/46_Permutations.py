""" L0: https://leetcode.com/problems/permutations/
find all permutations by dfs(P+[n], N[:i]+N[i+1:])
"""
# backtracking
class Solution:
    def permute(self, A: List[int]) -> List[List[int]]:
        ans = []
        stk = []
        def dfs(N):
            if not N: return ans.append(stk.copy())
            for i, n in enumerate(N):
                stk.append(n)
                dfs(N[:i]+N[i+1:])
                stk.pop()
    
        dfs(A)
        return ans
    
# dfs with states
class Solution:
    def permute(self, A: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(P, N):
            if len(P)==len(A): return self.ans.append(P)
            for i, n in enumerate(N):
                dfs(P+[n], N[:i]+N[i+1:])
    
        dfs([], A)
        return self.ans

# list(permutations(nums))
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rv = list(permutations(nums))
        for i in range(len(rv)):
            rv[i] = list(rv[i])
        return rv