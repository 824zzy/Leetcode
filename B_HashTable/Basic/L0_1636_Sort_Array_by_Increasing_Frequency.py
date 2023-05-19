""" https://leetcode.com/problems/sort-array-by-increasing-frequency/
1. count frequency of array
2. sort the array by frequency and key
"""
from header import *
class Solution:
    def frequencySort(self, A: List[int]) -> List[int]:
        cnt = Counter(A)
        ans = []
        for k, v in sorted(cnt.items(), key=lambda x: (x[1], -x[0])):
            ans.extend([k]*v)
        return ans