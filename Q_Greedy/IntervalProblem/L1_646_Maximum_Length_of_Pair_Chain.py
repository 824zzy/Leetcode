""" https://leetcode.com/problems/maximum-length-of-pair-chain/
non-overlap interval problem
"""
from header import *


class Solution:
    def findLongestChain(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: x[1])
        r = -1001
        ans = 0
        for a, b in A:
            if a > r:
                r = b
                ans += 1
        return ans


"""
[[1,2],[2,3],[3,4]]
[[1,2],[7,8],[4,5]]
[[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
[[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
"""
