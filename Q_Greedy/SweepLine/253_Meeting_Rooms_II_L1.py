""" https://leetcode.com/problems/meeting-rooms/
sweep line template
"""
from header import *

class Solution:
    def minMeetingRooms(self, A: List[List[int]]) -> int:
        SL = []
        for i, j in A:
            SL.append((i, 1))
            SL.append((j, -1))
        SL.sort()
        
        cnt = 0
        ans = 0
        for _, x in SL:
            cnt += x
            ans = max(ans, cnt)
        return ans