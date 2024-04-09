""" https://leetcode.com/problems/valid-permutations-for-di-sequence/submissions/
dp[i][x] means how many valid permutation of [0:i] s.t. the i-th element is x
TODO:
"""


class Solution:
    def numPermsDISequence(self, A: str) -> int:
        n = len(A)

        @cache
        def dp(i, x):
            if i == n:
                return 1
            if A[i] == 'D':
                if x == 0:
                    return 0
                return dp(i, x - 1) + dp(i + 1, x - 1)
            else:
                if x == n - i:
                    return 0
                return dp(i, x + 1) + dp(i + 1, x)

        return sum(dp(0, x) for x in range(n + 1)) % (10**9 + 7)
