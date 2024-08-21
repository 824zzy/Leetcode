""" https://leetcode.com/problems/stone-game-ii/
from ye15: https://leetcode.com/problems/stone-game-ii/discuss/530127/Python3-top-down-dp
Define dp(i, m) as the net winning stones when a player is at i with m. Let X and Y be Alex and Lee's stones respectively. Then,
X - Y = dp(0, 1) and X + Y = sum(piles).
As a result, X = (dp(0, 1) + sum(piles))//2.
"""

from header import *


class Solution:
    def stoneGameII(self, A: List[int]) -> int:
        @cache
        def dp(i, M):
            if i == len(A):
                return 0
            ans = -inf
            pre = A[i]
            for X in range(1, 2 * M + 1):
                ans = max(ans, pre - dp(i + X, max(M, X)))
                if i + X == len(A):
                    break
                pre += A[i + X]
            return ans

        return (dp(0, 1) + sum(A)) // 2
