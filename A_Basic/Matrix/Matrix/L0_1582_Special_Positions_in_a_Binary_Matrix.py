""" https://leetcode.com/problems/special-positions-in-a-binary-matrix/
simulation
"""
from header import *


class Solution:
    def numSpecial(self, A: List[List[int]]) -> int:
        r_cnt = defaultdict(int)
        c_cnt = defaultdict(int)

        for i, r in enumerate(A):
            r_cnt[i] = r.count(1)
        for i, c in enumerate(zip(*A)):
            c_cnt[i] = c.count(1)

        return sum(
            1
            for i in range(len(A))
            for j in range(len(A[0]))
            if r_cnt[i] == 1 and c_cnt[j] == 1 and A[i][j] == 1
        )
