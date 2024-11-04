""" https://leetcode.com/problems/number-of-longest-increasing-subsequence
LIS template with a counter to count the number of LIS.

Note that binary search + greedy is not applicable here because we need to count the number of LIS.
"""

from header import *


class Solution:
    def findNumberOfLIS(self, A: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(A))]
        for i in range(len(A)):
            cnt = 0
            for j in range(i):
                if A[j] < A[i]:
                    if dp[i][0] == dp[j][0] + 1:
                        cnt += dp[j][1]
                    elif dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        cnt = dp[j][1]
            dp[i][1] = cnt if cnt != 0 else 1
        mx = max([x for x, _ in dp])
        return sum([y for x, y in dp if x == mx])
