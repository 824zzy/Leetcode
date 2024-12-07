""" https://leetcode.com/problems/maximum-repeating-substring/
brute force with binary search
"""


class Solution:
    def maxRepeating(self, S: str, w: str) -> int:
        def fn(m):
            return w * m in S

        l, r = 1, len(S) // len(w) + 1
        while l < r:
            m = (l + r) // 2
            if not fn(m):
                r = m
            else:
                l = m + 1
        return l - 1
