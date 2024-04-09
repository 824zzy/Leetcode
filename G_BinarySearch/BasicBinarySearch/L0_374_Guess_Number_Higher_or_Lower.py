""" https://leetcode.com/problems/guess-number-higher-or-lower/
binary search template
"""


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n + 1
        while l < r:
            m = (l + r) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == -1:
                r = m
            else:
                l = m + 1
