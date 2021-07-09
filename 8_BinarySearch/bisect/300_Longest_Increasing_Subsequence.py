""" L2: LIS problem
use bisect to maintain a increasing list.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n, MAX = len(nums), float("inf")
        ends = [MAX for _ in range(n)]
        for v in nums:
            ends[bisect.bisect_left(ends, v)] = v
        return bisect.bisect_left(ends, MAX) if ends else 0