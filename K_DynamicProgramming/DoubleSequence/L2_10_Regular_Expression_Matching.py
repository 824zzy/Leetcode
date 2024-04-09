""" https://leetcode.com/problems/regular-expression-matching/submissions/
steal from ye: https://leetcode.com/problems/regular-expression-matching/discuss/652563/Python3-top-down-dp
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def fn(i, j):
            """Return True if s[i:] matches p[j:]"""
            if j == len(p):
                return i == len(s)
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                return fn(i, j + 2) or match and fn(i + 1, j)
            else:
                return match and fn(i + 1, j + 1)

        return fn(0, 0)
