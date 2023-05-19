""" https://leetcode.com/problems/most-frequent-even-element/
"""
from header import *

class Solution:
    def mostFrequentEven(self, A: List[int]) -> int:
        cnt = Counter([x for x in A if not x&1])
        cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
        if cnt: return cnt[0][0]
        else: return -1
        