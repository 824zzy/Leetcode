""" https://leetcode.com/problems/merge-intervals/
use sweep line/difference array to find left and right end points of the interval
"""
from header import *
class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        SL = []
        for i, j in A: SL.extend([[i, 1], [j, -1]])
        SL.sort(key=lambda x: (x[0], -x[1]))
        
        cnt = 0
        l, r = -1, -1
        ans = []
        
        for i in range(len(SL)):
            cnt += SL[i][1]
            if cnt==1 and l==-1: 
                l = SL[i][0]
            elif not cnt:
                r = SL[i][0]
                ans.append([l, r])
                l = -1
            
        return ans