""" L1: template
return r if the answer needs to be truncated.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l<=r:
            m = (l+r)//2
            if m*m==x:
                return m
            elif m*m>x:
                r = m - 1
            else:
                l = m + 1
        return r