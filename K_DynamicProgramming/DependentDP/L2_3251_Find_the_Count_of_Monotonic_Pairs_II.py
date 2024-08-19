""" https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/
"""

from header import *


class Solution:
    def countOfPairs(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(A)
        m = max(A)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(m + 1):
            dp[-1][i] = 1

        for i in range(n - 1, -1, -1):
            s = list(accumulate(dp[i + 1], initial=0))
            for pre1 in range(m + 1):
                if i == 0:
                    dp[i][pre1] = s[A[i] + 1] - s[pre1]
                else:
                    mn = max(pre1, A[i] - A[i - 1] + pre1)
                    mx = A[i] + 1
                    if mn <= mx:
                        x = s[mx] - s[mn]
                        dp[i][pre1] = x
        return dp[0][0] % mod


"""
[16,5]
[2,3,2]
[5,5,5,5]
[17,16]


1. x>=pre1
2. x<=A[i]
3. A[i-1]-pre1>=A[i]-x ==> x>=A[i]-A[i-1]+pre1
"""
