""" L0: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
find all subset by dfs(P^n, N[i+1:])
"""
class Solution:
    def subsetXORSum(self, A: List[int]) -> int:
        self.ans = 0
        
        def dfs(P, N):
            self.ans += P
            if not N: return
            for i, n in enumerate(N):
                dfs(P^n, N[i+1:])
        
        dfs(0, A)
        return self.ans