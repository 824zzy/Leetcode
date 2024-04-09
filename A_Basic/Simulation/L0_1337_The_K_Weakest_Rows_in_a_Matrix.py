""" https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
simulation
"""
from header import *


class Solution:
    def kWeakestRows(self, A: List[List[int]], k: int) -> List[int]:
        return [x for _, x in sorted((sum(x), i) for i, x in enumerate(A))[:k]]
