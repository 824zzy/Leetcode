""" https://leetcode.com/problems/can-place-flowers/
greedily find legal places by linear scan
"""
from header import *


class Solution:
    def canPlaceFlowers(self, A: List[int], n: int) -> bool:
        A = [0] + A + [0]
        for i in range(1, len(A) - 1):
            if A[i] == 0 and A[i - 1] == 0 and A[i + 1] == 0:
                A[i] = 1
                n -= 1
        return n <= 0
