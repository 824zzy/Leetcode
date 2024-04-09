""" https://leetcode.com/problems/missing-ranges
pairwise linear scan
"""
from header import *


class Solution:
    def findMissingRanges(self,
                          A: List[int],
                          l: int,
                          r: int) -> List[List[int]]:
        A = [l - 1] + A + [r + 1]
        ans = []
        for x, y in pairwise(A):
            if y - x > 1:
                ans.append([x + 1, y - 1])
        return ans


"""
[0,1,3,50,75]
0
99
[-1]
-1
-1
[]
1
1
"""
