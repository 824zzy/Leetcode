""" https://leetcode.com/problems/find-lucky-integer-in-an-array/
simulation
"""

from header import *


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cand = [k for k, v in Counter(arr).items() if k == v]
        return max(cand) if cand else -1
