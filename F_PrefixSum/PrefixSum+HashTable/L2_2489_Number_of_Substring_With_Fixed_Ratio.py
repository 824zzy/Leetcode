""" https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/description/
learned from ye: https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/solutions/2861416/c-java-python3-prefix-sum-freq-table/
"""
from header import *


class Solution:
    def fixedRatio(self, A: str, a: int, b: int) -> int:
        seen = Counter({0: 1})
        ans = 0
        prefix = 0

        for c in A:
            if c == '0':
                prefix += b
            else:
                prefix -= a
            ans += seen[prefix]
            seen[prefix] += 1
        return ans
