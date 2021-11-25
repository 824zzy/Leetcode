""" https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
Extend Kadane's algo by keeping track of max and min of subarray sum respectively.
"""
class Solution:
    def maxAbsoluteSum(self, A: List[int]) -> int:
        ans, maxS, minS = 0, 0, 0
        for x in A:
            maxS = max(0, maxS)+x
            minS = min(0, minS)+x
            ans = max(ans, maxS, -minS)
        return ans