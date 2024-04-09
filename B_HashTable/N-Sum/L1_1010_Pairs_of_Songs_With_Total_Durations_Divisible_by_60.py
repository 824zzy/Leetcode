""" https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
variance of two sum: (x+y)%60=0 => y%60=-x%60 => y=(-x%60)%60
"""
from header import *


class Solution:
    def numPairsDivisibleBy60(self, A: List[int]) -> int:
        cnt = Counter()
        ans = 0
        for x in A:
            x %= 60
            ans += cnt[(60 - x) % 60]
            cnt[x] += 1
        return ans
