""" https://leetcode.com/problems/count-sequences-to-k/
Memoized DFS with float state. At each index choose multiply, divide, or skip.
Since nums[i] is 1-6 and n<=19, the set of reachable float values is small
enough for @cache to work. The delta comparison handles potential float drift.

The cleaner approach (per hints) is DP on prime exponents: since 1-6 only
involve primes 2, 3, 5, represent val as (exp2, exp3, exp5) and track
exponents directly, avoiding floats entirely.
"""


class Solution:
    def countSequences(self, A: List[int], k: int) -> int:
        delta = 0.0001

        @cache
        def dfs(i, x):
            if i == len(A):
                return abs(x - k) < delta
            ans = 0
            ans += dfs(i + 1, x)
            ans += dfs(i + 1, x * A[i])
            ans += dfs(i + 1, x / A[i])
            return ans

        return dfs(0, 1)
