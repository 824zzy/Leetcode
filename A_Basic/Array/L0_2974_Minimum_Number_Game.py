""" https://leetcode.com/problems/minimum-number-game/
reading comprehension
1. sort the array
2. swap elements
"""
from header import *


class Solution:
    def numberGame(self, A: List[int]) -> List[int]:
        A.sort()
        for i in range(0, len(A), 2):
            A[i], A[i + 1] = A[i + 1], A[i]
        return A
