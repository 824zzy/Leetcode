""" https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
413 and 2110 are similar
"""


class Solution:
    def getDescentPeriods(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i == len(A) or A[i - 1] - 1 != A[i]:
                return 0
            return 1 + dp(i + 1)

        return len(A) + sum(dp(i) for i in range(1, len(A)))
