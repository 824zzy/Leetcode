""" https://leetcode.com/problems/find-champion-ii/
find the only node that in-degree is 0
"""
from header import *


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inD = [0] * n
        for i, j in edges:
            inD[j] += 1
        ans = [i for i, x in enumerate(inD) if x == 0]
        if len(ans) > 1:
            return -1
        else:
            return ans[0]
