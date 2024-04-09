""" https://leetcode.com/problems/number-of-distinct-roll-sequences/
Inspiration: "modulo 109 + 7" indicates that it is a DP problem.

The search space for each state is 1~6, and each state should follow two rules:
1. x is not in (pre0, pre1)
2. and gcd(x, pre0)==1

Time complexity: O(n*)
"""


class Solution:
    def distinctSequences(self, n: int) -> int:
        @cache
        def dp(i, pre0, pre1):
            if i == n:
                return 1
            ans = 0
            for x in range(1, 7):
                if x not in (pre0, pre1) and gcd(x, pre0) == 1:
                    ans += dp(i + 1, x, pre0)
            return ans % (10**9 + 7)

        return dp(0, -1, -1) % (10**9 + 7)
