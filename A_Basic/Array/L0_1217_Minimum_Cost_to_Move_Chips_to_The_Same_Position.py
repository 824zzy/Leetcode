""" https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
return minimum of odd count and even count
"""
class Solution:
    def minCostToMoveChips(self, P: List[int]) -> int:
        o, e = 0, 0
        for p in P:
            if p&1: o += 1
            else: e += 1
        return min(o, e)