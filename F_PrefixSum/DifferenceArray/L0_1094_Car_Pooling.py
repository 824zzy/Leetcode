""" https://leetcode.com/problems/car-pooling/
sweep line to greedily find max
"""
from header import *

# template 1


class Solution:
    def carPooling(self, A: List[List[int]], c: int) -> bool:
        A = [x for n, i, j in A for x in [[i, n], [j, -n]]]
        for i, v in sorted(A):
            c -= v
            if c < 0:
                return False
        return True


# template 2


class Solution:
    def carPooling(self, A: List[List[int]], c: int) -> bool:
        sl = [0] * 1001
        for n, i, j in A:
            sl[i] += n
            sl[j] -= n

        cnt = 0
        for x in sl:
            cnt += x
            if cnt > c:
                return False
        return True
