""" https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
use binary search to find if it is possible to make cnt bouquets in m days
"""
class Solution:
    def minDays(self, A: List[int], cnt: int, k: int) -> int:
        if len(A)<cnt*k: return -1
        def fn(m):
            kk = k
            _cnt = cnt
            for f in A:
                # find a flower
                if f<=m: kk -= 1
                else: kk = k
                # find a bouquet
                if not kk: _cnt, kk = _cnt-1, k
                # all cnt bouquets
                if not _cnt: return True
            return False
            
        l, r = 1, max(A)
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m + 1
        return l
    
    
class Solution:
    def minDays(self, A: List[int], cnt: int, k: int) -> int:
        if len(A)<cnt*k: return -1
        def fn(m):
            F = [1 if m>=a else 0 for a in A]
            F = [len(list(v)) for k, v in groupby(F) if k==1]
            c = 0
            for f in F: c += f//k
            return c>=cnt
            
        l, r = 1, max(A)
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m + 1
        return l