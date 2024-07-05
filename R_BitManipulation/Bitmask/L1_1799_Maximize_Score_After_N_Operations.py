""" https://leetcode.com/problems/maximize-score-after-n-operations/
since nums length is 14, we can use bitmask to represent the state of nums
"""
from header import *


class Solution:
    def maxScore(self, A: List[int]) -> int:
        n = len(A)

        @cache
        def dp(i, mask):
            if mask == (1 << n) - 1:
                return 0
            ans = 0
            for j in range(n):
                for jj in range(j + 1, n):
                    if j != jj and not mask & (1 << j) and not mask & (1 << jj):
                        ans = max(
                            ans,
                            gcd(A[j], A[jj]) * i
                            + dp(i + 1, mask ^ (1 << j) ^ (1 << jj)),
                        )
            return ans

        return dp(1, 0)


# backtracking method also works
class Solution:
    def maxScore(self, A: List[int]) -> int:
        def dfs(A, cands):
            if not A:
                cands.sort()
                return sum((i + 1) * c for i, c in enumerate(cands))
            ans = 0
            for i in range(1, len(A)):
                ans = max(ans, dfs(A[1:i] + A[i + 1 :], cands + [gcd(A[0], A[i])]))
            return ans

        return dfs(A, [])
