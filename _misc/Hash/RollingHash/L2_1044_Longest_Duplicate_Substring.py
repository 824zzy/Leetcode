""" https://leetcode.com/problems/longest-duplicate-substring/
binary search + rolling hash
"""


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        mod = 1_000_000_007

        def fn(k):
            """Return duplicated substring of length k."""
            p = pow(26, k, mod)
            hs = 0
            seen = {}
            for i, ch in enumerate(s):
                hs = (26 * hs + ord(ch) - 97) % mod
                if i >= k:
                    hs = (hs - (ord(s[i - k]) - 97) * p) % mod  # rolling hash
                if i + 1 >= k:
                    if hs in seen and s[i + 1 - k : i + 1] in seen[hs]:
                        return s[i + 1 - k : i + 1]  # resolve hash collision
                    seen.setdefault(hs, set()).add(s[i + 1 - k : i + 1])
            return ""

        l, r = 0, len(s) - 1
        while l < r:
            m = (l + r) // 2
            if not fn(m):
                r = m
            else:
                l = m + 1
        return fn(l + 1)
