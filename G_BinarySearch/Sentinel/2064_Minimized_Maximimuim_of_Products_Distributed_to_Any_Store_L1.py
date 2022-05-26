""" https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
the same as 
"""
class Solution:
    def minimizedMaximum(self, n: int, A: List[int]) -> int:
        def fn(m):
            """
            m: maximum products of a store
            cnt: how many stores we need
            """
            cnt = 0
            for x in A:
                cnt += ceil(x/m)
            return cnt<=n
            
        l, r = 1, max(A)
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m + 1
        return l