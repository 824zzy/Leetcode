""" https://leetcode.com/problems/count-number-of-homogenous-substrings/
solution 1: two pointers
solution 2: groupby
"""
from header import *


class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        s += "*"
        ans = 0
        i = 0
        for j in range(len(s)):
            if j and s[j] != s[j - 1]:
                l = j - i
                ans += l * (l + 1) // 2 % MOD
                i = j
        return ans


class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        A = [len(list(x)) for i, x in groupby(s)]
        return sum(x * (x + 1) // 2 for x in A) % MOD
