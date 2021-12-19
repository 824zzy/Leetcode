""" https://leetcode.com/problems/longest-increasing-subsequence/discuss/771027/Python3-binary-search
use bisect to maintain a increasing list.
O(NlogN)
"""
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        vals = []
        for x in A: 
            k = bisect_left(vals, x)
            if k == len(vals): vals.append(x)
            else: vals[k] = x
        return len(vals)