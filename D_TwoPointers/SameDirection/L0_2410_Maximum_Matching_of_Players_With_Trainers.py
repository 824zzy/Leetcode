""" https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
1. sort two arrays
2. greedily assign the smallest player to the smallest trainer by two pointers
"""
from header import *


class Solution:
    def matchPlayersAndTrainers(self, P: List[int], T: List[int]) -> int:
        P.sort()
        T.sort()
        i, j = 0, 0
        ans = 0
        while i < len(P) and j < len(T):
            if P[i] <= T[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        return ans
