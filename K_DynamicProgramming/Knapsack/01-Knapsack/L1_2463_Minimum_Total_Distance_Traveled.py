""" https://leetcode.com/problems/minimum-total-distance-traveled/solutions/
3D knap sack dp: for i-th robot, we can skip j-th factory or go to j-th factory if k is less than the limitation
"""

from header import *


class Solution:
    def minimumTotalDistance(self, R: List[int], F: List[List[int]]) -> int:
        R.sort()
        F.sort()

        @cache
        def dp(i, j, k):
            if i == len(R):
                return 0
            elif j == len(F):
                return inf
            # skip current factory
            ans = dp(i, j + 1, 0)
            # choose current factory
            # have space to repair robot
            if k < F[j][1]:
                ans = min(ans, dp(i + 1, j, k + 1) + abs(R[i] - F[j][0]))
            return ans

        return dp(0, 0, 0)
