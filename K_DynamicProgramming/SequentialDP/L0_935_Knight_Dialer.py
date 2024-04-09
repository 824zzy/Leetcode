""" https://leetcode.com/problems/knight-dialer/
sequential dp with hash table
"""
from header import *


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        MOD = 10**9 + 7
        dp = {x: 1 for x in range(10)}
        dp.pop(5)
        for _ in range(n - 1):
            _dp = dp.copy()
            _dp[0] = dp[4] + dp[6]
            _dp[1] = dp[6] + dp[8]
            _dp[2] = dp[7] + dp[9]
            _dp[3] = dp[4] + dp[8]
            _dp[4] = dp[0] + dp[3] + dp[9]
            _dp[6] = dp[0] + dp[1] + dp[7]
            _dp[7] = dp[2] + dp[6]
            _dp[8] = dp[1] + dp[3]
            _dp[9] = dp[2] + dp[4]
            _dp = {k: v % MOD for k, v in _dp.items()}
            dp = _dp
        return sum(dp.values()) % MOD


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        MOD = 10**9 + 7

        @cache
        def dp(i):
            if i == n:
                return {x: 1 for x in [0, 1, 2, 3, 4, 6, 7, 8, 9]}
            _dp = Counter()
            nxt = dp(i + 1)
            _dp[0] = nxt[4] + nxt[6]
            _dp[1] = nxt[6] + nxt[8]
            _dp[2] = nxt[7] + nxt[9]
            _dp[3] = nxt[4] + nxt[8]
            _dp[4] = nxt[0] + nxt[3] + nxt[9]
            _dp[6] = nxt[0] + nxt[1] + nxt[7]
            _dp[7] = nxt[2] + nxt[6]
            _dp[8] = nxt[1] + nxt[3]
            _dp[9] = nxt[2] + nxt[4]
            _dp = {k: v % MOD for k, v in _dp.items()}
            return _dp
        return sum(dp(1).values()) % MOD


"""
1
2
3131
"""
