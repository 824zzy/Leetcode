""" https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
count different types of garbage and their maximum distance separately
"""
from header import *

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = list(accumulate(travel, initial=0))
        g, p, m = 0, 0, 0
        gd, pd, md = 0, 0, 0
        for i, s in enumerate(garbage):
            if s.count('G'):
                g += s.count('G')
                gd = max(gd, travel[i])
            if s.count('P'):
                p += s.count('P')
                pd = max(pd, travel[i])
            if s.count('M'):
                m += s.count('M')
                md = max(md, travel[i])
        return g+p+m+gd+pd+md