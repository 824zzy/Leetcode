""" https://leetcode.com/problems/find-the-k-or-of-an-array/
loop through each bit and simulate
"""
from header import *

class Solution:
    def findKOr(self, A: List[int], k: int) -> int:
        ans = 0
        for i in range(31):
            if sum((x>>i)&1 for x in A) >= k:
                ans |= 1<<i
        return ans