""" https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
sort P and G by grow time, find maximum prefix+grow time. 
"""
from header import *

class Solution:
    def earliestFullBloom(self, P: List[int], G: List[int]) -> int:
        A = sorted(zip(P, G), key=lambda x: -x[1])
        ans = 0
        prefix = 0
        for p, g in A:
            prefix += p
            ans = max(ans, prefix+g)
        return ans