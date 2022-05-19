""" https://leetcode.com/problems/merge-intervals/
maintain a sorted list and update intervals
"""
from sortedcontainers import SortedList

class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        SL = SortedList()
        
        for l, r in A:
            k = SL.bisect_left([l, r])
            while k<len(SL) and SL[k][0]<=r:
                ll, rr = SL.pop(k)
                r = max(r, rr)
                
            if k and l<=SL[k-1][1]:
                ll, rr = SL.pop(k-1)
                l = ll
                r = max(r, rr)
            SL.add([l, r])
        return SL