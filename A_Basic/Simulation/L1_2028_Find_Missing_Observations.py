""" https://leetcode.com/problems/find-missing-observations/
simulation: assign each slot with n_sm // x, then adjust n_sm
"""

from header import *


class Solution:
    def missingRolls(self, roll: List[int], mean: int, n: int) -> List[int]:
        m_sm = sum(roll)
        all_sm = mean * (len(roll) + n)
        n_sm = all_sm - m_sm
        if n_sm / n > 6 or n_sm / n < 1:
            return []
        ans = []
        for x in range(n, 0, -1):
            ans.append(n_sm // x)
            n_sm -= n_sm // x
        return ans
