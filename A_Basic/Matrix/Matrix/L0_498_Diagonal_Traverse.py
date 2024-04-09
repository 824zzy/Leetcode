""" https://leetcode.com/problems/diagonal-traverse/
matrix + simulation
"""
from header import *


class Solution:
    def findDiagonalOrder(self, M: List[List[int]]) -> List[int]:
        m, n = len(M), len(M[0])
        mp = defaultdict(list)
        for i in range(m):
            for j in range(n):
                mp[i + j].append(M[i][j])
        ans = []
        for i, (_, v) in enumerate(mp.items()):
            if i & 1:
                ans.extend(v)
            else:
                ans.extend(v[::-1])
        return ans
