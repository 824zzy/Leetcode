""" https://leetcode.com/problems/count-pairs-of-similar-strings/description/
count similar pairs by Counter and the pairs are v*(v-1)//2
"""
from header import *
class Solution:
    def similarPairs(self, A: List[str]) -> int:
        cnt = [tuple(sorted(set(x))) for x in A]
        ans = 0
        for _, v in Counter(cnt).items():
            ans += v*(v-1)//2
        return ans 