""" https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/
update max and prefix sum at the same time
"""
from header import *

class Solution:
    def findPrefixScore(self, A: List[int]) -> List[int]:
        ans = []
        mx = 0
        pre_sum = 0
        for x in A:
            mx = max(mx, x)
            pre_sum += x+mx
            ans.append(pre_sum)
        return ans