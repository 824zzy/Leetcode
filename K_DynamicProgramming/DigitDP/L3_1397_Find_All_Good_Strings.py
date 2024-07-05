""" https://leetcode.com/problems/find-all-good-strings/
from: https://leetcode.cn/problems/find-all-good-strings/solution/by-jmy45-r5j1/
digit DP + KMP
"""
from header import *


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        # KMP求next
        e = evil
        evil = " " + evil
        sz = len(e)
        ne = [0] * (sz + 1)
        j = 0
        for i in range(2, sz + 1):
            while j and evil[i] != evil[j + 1]:
                j = ne[j]
            if evil[i] == evil[j + 1]:
                j += 1
            ne[i] = j

        @cache
        def f(i: int, j: int, is_limit: bool, s: str) -> int:
            if i == n:
                return 1
            up = ord(s[i]) if is_limit else 122
            ans = 0
            for d in range(97, up + 1):
                x = chr(d)
                k = j
                while k and x != evil[k + 1]:
                    k = ne[k]
                if x == evil[k + 1]:
                    k += 1
                if k == sz:
                    continue
                ans += f(i + 1, k, is_limit and d == up, s)
            return ans

        return (f(0, 0, True, s2) - f(0, 0, True, s1) + (e not in s1)) % (10 ** 9 + 7)
