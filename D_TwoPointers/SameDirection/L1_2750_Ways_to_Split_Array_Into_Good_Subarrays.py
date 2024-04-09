""" https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/
1. it is not dp
2. multiply all the possible splits
"""
from header import *
from functools import reduce

# elegant two pointer solution from 0x3ff


class Solution:
    def numberOfGoodSubarraySplits(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        ans = 1
        pre = -1
        for i, x in enumerate(A):
            if x == 0:
                continue
            if pre != -1:
                ans = ans * (i - pre) % MOD
            pre = i
        return ans if pre >= 0 else 0

# use groupby


class Solution:
    def numberOfGoodSubarraySplits(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        ans = []
        while A and A[0] == 0:
            A.pop(0)
        A = [(k, len(list(v))) for k, v in groupby(A)]
        for i, (_, x) in enumerate(A):
            if i & 1 and i + 1 < len(A):
                ans.append(x + 1)
        if ans:
            return reduce(mul, ans) % MOD
        else:
            return 1 if len(A) > 0 else 0


# Use 01 knapsack, but not efficient
class Solution:
    def numberOfGoodSubarraySplits(self, A: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(i, hasOne):
            if i == len(A):
                return int(hasOne)
            ans = 0
            if A[i] == 0:
                ans += dp(i + 1, hasOne)  # do nothing
                if hasOne:
                    ans += dp(i + 1, False)  # split
            else:
                ans = dp(i + 1, True)
            return ans % MOD
        return dp(0, False)
