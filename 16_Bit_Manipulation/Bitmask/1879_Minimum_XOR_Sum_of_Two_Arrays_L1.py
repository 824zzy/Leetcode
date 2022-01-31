""" https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
"""
class Solution:
    def minimumXORSum(self, A: List[int], B: List[int]) -> int:
        @cache
        def dfs(mask, i):
            if i==len(A): return 0
            ans = []
            for j in range(len(A)):
                if mask & 1<<j:
                    ans.append((A[i]^B[j])+dfs(mask ^ 1<<j, i+1))
            return min(ans)
        
        return dfs((1<<len(A))-1, 0)