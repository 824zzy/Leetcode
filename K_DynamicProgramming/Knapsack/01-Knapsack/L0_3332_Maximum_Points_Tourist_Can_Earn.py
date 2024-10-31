""" https://leetcode.com/problems/maximum-points-tourist-can-earn/
reading comprehension + knap sack dp
"""

from header import *


class Solution:
    def maxScore(
        self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]
    ) -> int:
        @cache
        def dp(i, curr):
            if i == k:
                return 0
            # stay
            ans = stayScore[i][curr] + dp(i + 1, curr)
            # move
            for dest in range(n):
                ans = max(ans, travelScore[curr][dest] + dp(i + 1, dest))
            return ans

        return max(dp(0, x) for x in range(n))
