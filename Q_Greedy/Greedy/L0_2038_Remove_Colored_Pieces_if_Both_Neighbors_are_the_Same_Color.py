""" https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
groupby the colors and count triple "A" or "B"
"""
from header import *


class Solution:
    def winnerOfGame(self, A: str) -> bool:
        A = [(k, len(list(v))) for k, v in groupby(A)]
        a, b = 0, 0
        for k, v in A:
            if v >= 3:
                if k == "A":
                    a += v - 2
                else:
                    b += v - 2
        return a > b
