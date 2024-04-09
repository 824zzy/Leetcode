""" https://leetcode.com/problems/longest-common-subpath/
https://leetcode.com/problems/longest-common-subpath/discuss/1496426/Python3-rolling-hash
"""


class RabinKarp:

    def __init__(self, s):
        """Calculate rolling hash of s"""
        self.m = 1_111_111_111_111_111_111
        self.pow = [1]
        self.roll = [0]  # rolling hash

        p = 1_000_000_007
        for x in s:
            self.pow.append(self.pow[-1] * p % self.m)
            self.roll.append((self.roll[-1] * p + x) % self.m)

    def query(self, i, j):
        """Return rolling hash of s[i:j]"""
        return (self.roll[j] - self.roll[i] * self.pow[j - i]) % self.m


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        rks = [RabinKarp(x) for x in paths]

        def fn(x):
            seen = set()
            for rk, path in zip(rks, paths):
                vals = {rk.query(i, i + x) for i in range(len(path) - x + 1)}
                # print(x, seen, vals)
                if not seen:
                    seen = vals
                else:
                    seen &= vals
                if not seen:
                    return False
            return True

        mi_path = min([p for p in paths], key=len)
        l, r = 0, len(mi_path) + 1
        while l < r:
            m = (l + r) // 2
            if not fn(m):
                r = m
            else:
                l = m + 1
        return l - 1
