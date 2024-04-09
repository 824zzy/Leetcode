""" https://leetcode.com/problems/gas-station/
heuristic:
1. All valid prefix sum should be not negative.
2. If we get negative prefix sum, it means we can not succeed using current starting index,
and we need to take next as starting index.
"""
from header import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        sm = 0
        i = 0
        for j in range(n):
            sm += gas[j] - cost[j]
            if sm < 0:
                i = j + 1
                sm = 0
        return i
