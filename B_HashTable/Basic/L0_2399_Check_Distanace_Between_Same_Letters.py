""" https://leetcode.com/problems/check-distances-between-same-letters/
use hash table to store the index of each letter, then check if all the distances are valid
"""
from header import *


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        mp = defaultdict(list)
        for i, x in enumerate(s):
            mp[ord(x) - 97].append(i)

        for i in range(len(distance)):
            if mp[i] and mp[i][1] - mp[i][0] != distance[i] + 1:
                return False
        return True
