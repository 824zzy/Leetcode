""" https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/
1. use hash table to find all the modulus
2. greedily check every number until we can a unachievable one
"""
from header import *


class Solution:
    def findSmallestInteger(self, A: List[int], value: int) -> int:
        cnt = Counter()
        for x in A:
            cnt[x % value] += 1
        for i in range(len(A) + 100):
            if cnt[i % value] != 0:
                cnt[i % value] -= 1
            else:
                return i
