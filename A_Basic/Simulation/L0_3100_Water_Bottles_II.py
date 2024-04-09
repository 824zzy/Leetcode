""" https://leetcode.com/problems/water-bottles/
simulation based on the problem statement
"""


class Solution:
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        res = n
        while n >= e:
            n = n - e + 1
            e += 1
            res += 1
        return res
