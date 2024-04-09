""" https://leetcode.com/problems/line-reflection/
Find the center and check if the reflected points (2*avg-x) exist.
"""
from header import *


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        mp = defaultdict(set)
        for x, y in points:
            mp[y].add(x)

        ans = set()
        for _, v in mp.items():
            avg = sum(v) / len(v)
            for vv in v:
                if avg * 2 - vv not in v:
                    return False
            ans.add(avg)
        return len(ans) == 1


"""
[[1,1],[-1,1]]
[[1,1],[-1,-1]]
[[0,0]]
[[0,0],[1,0],[3,0]]
[[0,0],[1,0]]
[[-16,1],[16,1],[16,1]]
"""
