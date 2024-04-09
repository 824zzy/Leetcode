""" https://leetcode.com/problems/super-pow/
divide b into two parts and conquer them
"""
from header import *


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int(str(''.join(map(str, b))))

        @cache
        def dfs(x):
            if x == 1:
                return a
            if x & 1:
                return dfs(x // 2) * dfs(x // 2 + 1) % 1337
            else:
                return dfs(x // 2) * dfs(x // 2) % 1337
        return dfs(b)


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int(str(''.join(map(str, b)))), 1337)
