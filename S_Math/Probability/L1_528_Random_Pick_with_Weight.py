""" https://leetcode.com/problems/random-pick-with-weight/
Probability == prefix sum + binary search

zillow interview problem
"""
from header import *


class Solution:
    def __init__(self, w: List[int]):
        self.prefix = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.prefix, randint(1, self.prefix[-1]))
