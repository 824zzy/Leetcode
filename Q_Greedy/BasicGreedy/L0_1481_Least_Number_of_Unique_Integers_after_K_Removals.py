""" https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
greedy minus least frequent elements from k
"""
from header import *

class Solution:
    def findLeastNumOfUniqueInts(self, A: List[int], k: int) -> int:
        ans = 0
        for _, v in sorted(Counter(A).items(), key=lambda x: x[1]):
            if v<=k: k -= v
            else: ans += 1
        return ans