""" https://leetcode.com/problems/best-team-with-no-conflicts/
1. sort the players by age
2. find the longest increasing subsequence
"""
from header import *


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        A = [s for _, s in sorted(zip(ages, scores))]

        @cache
        def dp(i):
            if i == len(A):
                return 0
            ans = A[i]
            for j in range(i):
                if A[j] <= A[i]:
                    ans = max(ans, A[i] + dp(j))
            return ans

        return max(dp(i) for i in range(len(A)))
