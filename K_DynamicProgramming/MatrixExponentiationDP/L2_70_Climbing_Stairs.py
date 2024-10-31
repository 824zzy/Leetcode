""" https://leetcode.com/problems/climbing-stairs/
1. matrix exponentiation DP
    f(n) = M^t * f(0)
    ==>
    [f(n-1), f(n)] = M^t * [f(1), f(2)]
    M = [[0, 1], [1, 1]]

2. linear DP
    dp[i] = dp[i-1] + dp[i-2]
"""

from header import *


# matrix exponentiation DP: Time complexity O(logn)
class Solution:
    def climbStairs(self, n: int) -> int:
        def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            return [
                [sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a
            ]

        def pow_mul(a: List[List[int]], n: int, f0: List[List[int]]) -> List[List[int]]:
            res = f0
            while n:
                if n & 1:
                    res = mul(a, res)
                a = mul(a, a)
                n >>= 1
            return res

        f0 = [[1], [2]]
        M = [[0, 1], [1, 1]]
        fn = pow_mul(M, n - 1, f0)
        return fn[0][0]


# bottom up linear DP: Time complexity O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# top down linear DP: Time complexity O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 2:
                return 2
            if i == 1:
                return 1
            return dp(i - 1) + dp(i - 2)

        return dp(n)
