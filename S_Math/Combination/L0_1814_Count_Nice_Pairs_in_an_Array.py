""" https://leetcode.com/problems/count-nice-pairs-in-an-array/description/
Observation: x+rev(y) = y+rev(x) => x-rev(x) = y-rev(y)

So just count the combinations of x-rev(x) in pairs.
"""
from header import *

class Solution:
    def countNicePairs(self, A: List[int]) -> int:
        cnt = Counter([x-int(str(x)[::-1]) for x in A])
        return sum([comb(k, 2) for k in cnt.values()])%(10**9+7)