""" https://leetcode.com/problems/number-of-pairs-satisfying-inequality/
Given nums1[i]-nums2[i]<=nums1[j]-nums2[j]+diff, we can obtain (nums1[i]-nums2[i])<=(nums1[j]-nums2[j])+diff
1. calculate difference array
2. use a sorted list to find how many elements are smaller or equal(bisect_right) than (nums1[j]-nums2[j])+diff
"""
from header import *

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        A = [nums1[i]-nums2[i] for i in range(len(nums1))]
        SL = SortedList()
        ans = 0
        for x in A:
            ans += SL.bisect_right(x+diff)
            SL.add(x)
        return ans