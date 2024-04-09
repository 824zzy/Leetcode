""" https://leetcode.com/problems/uncrossed-lines/
Same as longest common subsequence problem.
"""
from header import *


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        @cache
        def dp(i, j):
            if i == len(A) or j == len(B):
                return 0
            ans = max(dp(i, j + 1), dp(i + 1, j))
            if A[i] == B[j]:
                ans = max(ans, 1 + dp(i + 1, j + 1))
            return ans

        return dp(0, 0)


"""
2 2 1 4 2
1 2 2 2 4
"""
