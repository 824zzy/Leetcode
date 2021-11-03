""" L0: https://leetcode.com/problems/permutations/
find all permutations by dfs(P+[n], N[:i]+N[i+1:])
"""
# Backtracking
class Solution:
    def permute(self, A: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(P, N):
            if len(P)==len(A):
                self.ans.append(P)
                return
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