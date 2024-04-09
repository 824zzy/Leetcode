""" https://leetcode.com/problems/count-the-number-of-k-big-indices/
sorted list + binary search

note that A.bisect_left(x) is way much faster than bisect_left(A, x)
"""
from header import *


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        A = SortedList()
        pre = [0] * len(nums)
        for i, x in enumerate(nums):
            pre[i] = A.bisect_left(x)
            A.add(x)

        B = SortedList()
        suf = [0] * len(nums)
        for i, x in enumerate(reversed(nums)):
            suf[i] = B.bisect_left(x)
            B.add(x)

        ans = 0
        for p, s in zip(pre, reversed(suf)):
            if p >= k and s >= k:
                ans += 1
        return ans
