""" https://leetcode.com/problems/find-champion-i/
problem description is unclear;
brute force to find the strongest team;
"""
from header import *


class Solution:
    def findChampion(self, G: List[List[int]]) -> int:
        A = [(sum(x), i) for i, x in enumerate(G)]
        return max(A)[1]
