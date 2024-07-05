# Using heap: 304ms
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        N, m, S = [1], 1, set()
        for _ in range(n):
            while m in S:
                m = heapq.heappop(N)
            S.add(m)
            for i in 2, 3, 5:
                heapq.heappush(N, i * m)
        return m


# Dynamic Programming


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        i = j = k = 0
        for c in range(1, n):
            dp[c] = min(dp[i] * 2, dp[j] * 3, dp[k] * 5)
            if dp[c] == dp[i] * 2:
                i += 1
            if dp[c] == dp[j] * 3:
                j += 1
            if dp[c] == dp[k] * 5:
                k += 1
        return dp[-1]
