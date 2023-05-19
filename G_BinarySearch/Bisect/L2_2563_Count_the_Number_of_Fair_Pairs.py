""" https://leetcode.com/problems/count-the-number-of-fair-pairs/
lower <= x+y <= upper ==> lower-x <= y <= upper-x
"""
from header import *

class Solution:
    def countFairPairs(self, A: List[int], lower: int, upper: int) -> int:
        A.sort()
        ans = 0
        for i, x in enumerate(A):
            l = bisect_left(A, lower-x, 0, i)
            r = bisect_right(A, upper-x, 0, i)
            ans += r - l
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