""" https://leetcode.com/problems/split-array-largest-sum/
the same at 1011
"""
class Solution:
    def splitArray(self, A: List[int], N: int) -> int:
        def feasible(m):
            s, n = 0, 1
            for a in A:
                if s+a>m:
                    s, n = 0, n+1
                    if n>N: return False
                s += a
            return True
            
            
        l, r = max(A), sum(A)
        while l<=r:
            m = (l+r)//2
            if not feasible(m): l = m+1
            else: r = m-1
        return l