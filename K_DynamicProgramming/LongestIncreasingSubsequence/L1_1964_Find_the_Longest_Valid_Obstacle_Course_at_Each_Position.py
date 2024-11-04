""" https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
The same as 300.
"""
from header import *


class Solution:
    def longestObstacleCourseAtEachPosition(self, A: List[int]) -> List[int]:
        vals = []
        ans = []
        for x in A:
            k = bisect_right(vals, x)
            ans.append(k + 1)
            if k == len(vals):
                vals.append(x)
            else:
                vals[k] = x
        return ans
