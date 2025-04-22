""" https://leetcode.com/problems/maximize-active-section-with-trade-i/
group by trick + enumeration
"""
from header import *

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        sm = s.count('1')
        s = '1'+s+'1'
        A = [len(list(v)) for k, v in groupby(s)]
        ans = sm
        for i in range(2, len(A)-2):
            if i&1==0:
                ans = max(ans, sm+A[i-1]+A[i+1])
        return ans

"""
sm-A[i] + (A[i-1]+A[i]+A[i+1])

"11010110"
==>"1110101101"
"""