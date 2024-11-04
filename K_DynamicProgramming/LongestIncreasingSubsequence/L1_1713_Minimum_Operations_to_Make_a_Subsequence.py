""" https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/
LIS template + hash table
"""

from header import *


class Solution:
    def minOperations(self, T: List[int], A: List[int]) -> int:
        v2i = {x: i for i, x in enumerate(T)}

        dp = []
        for x in A:
            if x not in v2i:
                continue
            k = bisect_left(dp, v2i[x])
            if k == len(dp):
                dp.append(v2i[x])
            else:
                dp[k] = v2i[x]
        return len(T) - len(dp)
