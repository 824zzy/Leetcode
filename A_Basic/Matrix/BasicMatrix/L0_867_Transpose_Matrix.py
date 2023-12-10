""" https://leetcode.com/problems/transpose-matrix/
basic usage of zip(*A)
"""
from header import *

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [x for x in zip(*A)]