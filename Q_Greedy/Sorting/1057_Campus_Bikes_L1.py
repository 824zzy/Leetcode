""" https://leetcode.com/problems/campus-bikes/description/
greedily assign bikes to workers
"""
from header import *
class Solution:
    def assignBikes(self, W: List[List[int]], B: List[List[int]]) -> List[int]:
        D = []
        for i, (x1, y1) in enumerate(W):
            for j, (x2, y2) in enumerate(B):
                D.append((abs(x1-x2)+abs(y1-y2), i, j))
        seenb = set()
        seenw = set()
        ans = [0]*len(W)
        for _, i, j in sorted(D):
            if j not in seenb and i not in seenw:
                ans[i] = j
                seenb.add(j)
                seenw.add(i)
        return ans