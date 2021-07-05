""" L2
lower<=sorted_sum[i]-sorted_sum[j]<=upper
==>
sorted_sum[i]-upper<=sorted_sum[j]
sorted_sum[i]-lower>=sorted_sum[j]
"""
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
