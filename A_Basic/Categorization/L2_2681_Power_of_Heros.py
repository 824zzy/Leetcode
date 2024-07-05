""" https://leetcode.com/problems/power-of-heroes
1. sort the array
2. find patterns of how each element contribute to the final answer
"""
from header import *


class Solution:
    def sumOfPower(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        sm = 0
        for x in A:
            ans = (ans + x ** 3 + x ** 2 * sm) % (10 ** 9 + 7)
            sm = (2 * sm + x) % (10 ** 9 + 7)
        return ans


"""
[1,2,4]

"""
