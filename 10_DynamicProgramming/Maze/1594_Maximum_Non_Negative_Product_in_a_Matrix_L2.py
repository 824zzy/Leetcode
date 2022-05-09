""" https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
solution from ye: Return maximum & minimum products ending at (i, j).
"""
class Solution:
    def maxProductPath(self, A: List[List[int]]) -> int:
        MOD = 10**9+7
        @cache
        def dp(i, j):
            if not (0<=i<len(A) and 0<=j<len(A[0])): return -inf, inf
            if i==len(A)-1 and j==len(A[0])-1: return A[i][j], A[i][j]
            mx1, mn1 = dp(i+1, j)
            mx2, mn2 = dp(i, j+1)
            mx, mn = max(mx1, mx2)*A[i][j], min(mn1, mn2)*A[i][j]
            if A[i][j]>0: return (mx, mn)
            else: return (mn, mx)
        
        mx, _ = dp(0, 0)
        if mx>=0: return mx%MOD
        else: return -1