""" https://leetcode.com/problems/count-sorted-vowel-strings/
"""
from functools import reduce


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 4, 4)


class Solution:
    def countVowelStrings(self, n: int) -> int:
        def factor(i):
            return reduce(lambda x, y: x * y, range(1, i + 1))

        return int(factor(n + 4) / (factor(4) * factor(n)))
