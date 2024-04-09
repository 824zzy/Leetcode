""" https://leetcode.com/problems/squirrel-simulation/
two pass + enumeration
"""
from header import *


class Solution:
    def minDistance(self,
                    height: int,
                    width: int,
                    tree: List[int],
                    squirrel: List[int],
                    A: List[List[int]]) -> int:
        sm = 0
        for x, y in A:
            sm += 2 * (abs(tree[0] - x) + abs(tree[1] - y))
        ans = inf
        for x, y in A:
            ans = min(ans, sm - abs(tree[0] - x) - abs(tree[1] -
                      y) + abs(squirrel[0] - x) + abs(squirrel[1] - y))
        return ans
