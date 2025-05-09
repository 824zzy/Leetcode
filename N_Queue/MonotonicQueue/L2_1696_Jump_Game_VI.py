""" https://leetcode.com/problems/jump-game-vi/
DP + monotonic queue

Given the transition function:
    dp[i] = max(A[i]+dp[i+1], ...  A[i+k-2]+dp[i+k-1], A[i+k-1]+dp[i+k])
The transition function is calculating the maximum value of the subarray starting from i. (subarray maximum)
==> Use a monotonic queue to optimize the DP.
"""

from header import *


# Top-down DP O(n*k)
class Solution:
    def maxResult(self, A: List[int], k: int) -> int:
        @cache
        def dp(i):
            if i >= len(A):
                return 0
            ans = -inf
            for j in range(i, min(i + k, len(A))):
                ans = max(ans, A[j] + dp(j + 1))
            return ans

        return dp(0) if dp(0) != -inf else 0


# Bottom-up DP O(n*k)
class Solution:
    def maxResult(self, A: List[int], k: int) -> int:
        dp = [-inf] * (len(A) + 1)
        dp[-1] = 0
        for i in reversed(range(len(A))):
            for j in range(i, min(i + k, len(A))):
                dp[i] = max(dp[i], A[j] + dp[j + 1])
        return dp[0] if dp[0] != -inf else 0


# Data structure optimization O(nlogk)
class Solution:
    def maxResult(self, A: List[int], k: int) -> int:
        dq = deque([(0, A[0])])
        for i in range(1, len(A)):
            while dq and i - dq[0][0] > k:
                dq.popleft()
            mx_score = dq[0][1] + A[i]
            while dq and dq[-1][1] < mx_score:
                dq.pop()
            dq.append((i, mx_score))
        return dq[-1][1]
