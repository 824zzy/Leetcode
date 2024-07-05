""" https://leetcode.com/problems/longest-arithmetic-subsequence/
At any A[i], go through the values seen already (xx) and check the length
of arithmetic sequence ending at x with step A[j]-A[i]. Return the maximum length.
"""
from header import *

# bottom up


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [defaultdict(lambda: 1) for _ in range(len(A))]
        ans = 0
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[j][diff] + 1
            ans = max(ans, max(dp[i].values()))
        return ans


# top down solution


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        @cache
        def dp(i):
            cnt = defaultdict(lambda: 1)
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                cnt[diff] = max(cnt[diff], 1 + dp(j)[diff])
            return cnt

        return max(max(dp(i).values()) for i in range(len(A)))
