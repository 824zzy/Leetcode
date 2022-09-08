""" https://leetcode.com/problems/shuffle-the-array/
rearrange array based on parity
"""
from header import *

class Solution:
    def shuffle(self, A: List[int], n: int) -> List[int]:
        A[::2] = A[:n]
        A[1::2] = A[n:]
        return A