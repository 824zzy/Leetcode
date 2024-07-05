""" https://leetcode.com/problems/flipping-an-image/
bit simulation
"""
from header import *


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[n ^ 1 for n in a][::-1] for a in A]
