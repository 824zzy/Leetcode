""" https://leetcode.com/problems/2-keys-keyboard/

"""


class Solution:
    def minSteps(self, n: int) -> int:

        @cache
        def dfs(n):
            """Return the minimum number of steps to get n 'A's."""
            if n == 1:
                return 0
            return min(
                dfs(i) +
                n //
                i for i in range(
                    1,
                    n //
                    2 +
                    1) if n %
                i == 0)

        return dfs(n)
