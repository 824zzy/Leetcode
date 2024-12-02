""" https://leetcode.com/problems/check-if-n-and-its-double-exist/
set look up
"""

from header import *


class Solution:
    def checkIfExist(self, A: List[int]) -> bool:
        seen = set()
        for x in A:
            if x * 2 in seen or (x & 1 == 0 and x // 2 in seen):
                return True
            seen.add(x)
        return False
