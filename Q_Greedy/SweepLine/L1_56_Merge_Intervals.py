""" https://leetcode.com/problems/merge-intervals/
use sweep line/difference array to find left and right end points of the interval
"""
from header import *

class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        sl = []
        for i, j in A:
            sl.append((i, 1))
            sl.append((j+1, -1))
        sl.sort()
        
        cnt = 0
        ans = []
        l = None
        for i, x in sl:
            if l==None:
                l = i
            cnt += x
            if cnt==0:
                ans.append([l, i-1])
                l = None
        return ans