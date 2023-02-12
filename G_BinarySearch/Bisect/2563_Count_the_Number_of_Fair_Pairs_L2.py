""" https://leetcode.com/problems/count-the-number-of-fair-pairs/
"""
from header import *

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        A = []
        for x in nums:
            l, r = lower-x, upper-x
            ll = bisect_left(A, l)
            rr = bisect_right(A, r)
            A.append(x)
            ans += rr-ll
        return ans
    
"""
[0,1,7,4,4,5]
3
6
[1,7,9,2,5]
11
11
[0,0,0,0,0,0]
0
0
"""