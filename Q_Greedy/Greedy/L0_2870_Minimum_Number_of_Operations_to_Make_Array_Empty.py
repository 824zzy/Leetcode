""" https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
greedy
"""
from header import *


class Solution:
    def minOperations(self, A: List[int]) -> int:
        ans = 0
        for _, v in Counter(A).items():
            if v == 1:
                return -1
            else:
                ans += ceil(v / 3)
        return ans


""" https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
sequential DP
"""


class Solution:
    def minOperations(self, A: List[int]) -> int:
        A.sort()

        @cache
        def dp(i):
            if i >= len(A):
                return 0
            ans = inf
            # delete 2
            if i + 1 < len(A) and A[i] == A[i + 1]:
                ans = min(ans, 1 + dp(i + 2))
            # delete 3
            if i + 2 < len(A) and A[i] == A[i + 1] and A[i + 1] == A[i + 2]:
                ans = min(ans, 1 + dp(i + 3))
            return ans

        ans = dp(0)
        return ans if ans != inf else -1
