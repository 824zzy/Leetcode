""" https://leetcode.com/problems/number-of-great-partitions/
solve it reversely: find partition that sum of the elements of any group is less than k
"""
from header import *


class Solution:
    def countPartitions(self, A: List[int], k: int) -> int:
        if sum(A) < 2 * k:
            return 0

        @cache
        def dp(i, k):
            if k <= 0:
                return 0
            if i == len(A):
                return k > 0
            # skip
            ans = dp(i + 1, k)
            # choose
            ans += dp(i + 1, k - A[i])
            return ans % (10 ** 9 + 7)

        return (2 ** len(A) - dp(0, k) * 2) % (10 ** 9 + 7)
