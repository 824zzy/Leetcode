""" https://leetcode.com/problems/slowest-key/
Simulation & Reading comprehension
"""

from header import *


class Solution:
    def slowestKey(self, T: List[int], P: str) -> str:
        T = [0] + T
        f, c = 0, "a"
        for i, (t1, t2) in enumerate(pairwise(T)):
            if t2 - t1 > f:
                f = t2 - t1
                c = P[i]
            elif t2 - t1 == f:
                c = max(P[i], c)
        return c


"""
[9,29,49,50]
"cbcd"
[12,23,36,46,62]
"spuda"
[9,29,49,50]
"cbcd"
[1,2,3]
"aba"
[19,22,28,29,66,81,93,97]
"fnfaaxha"
"""
