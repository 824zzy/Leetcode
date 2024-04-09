""" https://leetcode.com/problems/smallest-sufficient-team/
bitmask + knapsack
"""
from header import *


class Solution:
    def smallestSufficientTeam(self,
                               req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        A = {x: i for i, x in enumerate(req_skills)}
        P = []
        for p in people:
            tmp = 0
            for s in p:
                tmp |= 1 << A[s]
            P.append(tmp)

        @cache
        def dp(i, mask):
            if mask == (1 << len(req_skills)) - 1:
                return []
            if i == len(P):
                return [0] * 100
            ans1 = dp(i + 1, mask)
            ans2 = dp(i + 1, mask | P[i])
            return min(ans1, [i] + ans2, key=len)

        return dp(0, 0)
