""" https://leetcode.com/problems/meeting-rooms/
sweep line template
"""
from header import *


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        diff = []
        for i, j in intervals:
            diff.append((i, 1))
            diff.append((j, -1))
        diff.sort()

        cnt = 0
        res = 0
        for _, i in diff:
            cnt += i
            res = max(res, cnt)
        return res
