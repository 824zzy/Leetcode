""" https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
the same as 410
search final answer rather than index
"""
class Solution:
    def splitArray(self, A: List[int], n: int) -> int:
        def fn(m, n):
            _m = m
            for x in A:
                if _m-x>=0: _m -= x
                else: _m, n = m-x, n-1
            return n>0
            
        l, r = max(A), sum(A)
        while l<r:
            m = (l+r)//2
            if fn(m, n): r = m
            else: l = m + 1
        return l