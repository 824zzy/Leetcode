""" https://leetcode.com/problems/count-of-range-sum/
lower<=presum[j]-presum[i]<=upper
==>
presum[j]-upper<=presum[i]<=presum[j]-lower
"""
from header import *

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        count, s = 0, 0
        sorted_sums = [0]
        for x in nums:
            s += x
            l = bisect.bisect_left(sorted_sums, s - upper)
            r = bisect.bisect_right(sorted_sums, s - lower)
            count += r - l
            bisect.insort(sorted_sums, s)
        return count