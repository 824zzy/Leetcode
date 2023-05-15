""" https://leetcode.com/problems/number-of-senior-citizens/
simulation
"""
from header import *

class Solution:
    def countSeniors(self, A: List[str]) -> int:
        ans = 0
        for a in A:
            y = int(a[-4:-2])
            if y>60:
                ans += 1
        return ans