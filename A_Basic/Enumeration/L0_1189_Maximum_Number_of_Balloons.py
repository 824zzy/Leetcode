""" https://leetcode.com/problems/maximum-number-of-balloons/
enumerate "balloon" and find the minimum count of each letter in s
"""
from header import *


class Solution:
    def maxNumberOfBalloons(self, s: str) -> int:
        cnt = Counter(s)
        t = Counter("balloon")
        ans = inf
        for k, v in t.items():
            if k not in cnt:
                return 0
            else:
                ans = min(ans, cnt[k] // v)
        return ans
