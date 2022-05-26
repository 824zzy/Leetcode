""" https://leetcode.com/problems/maximum-sum-circular-subarray/
compute both maximum contiguous subarray and minimum contiguous subarray
"""
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        ma, cur_ma = -inf, 0
        mi, cur_mi = -inf, 0
        for x in A:
            cur_ma = max(0, cur_ma)+x
            ma = max(ma, cur_ma)
            
            cur_mi = max(0, cur_mi)-x
            mi = max(mi, cur_mi)
        
        if ma<0: return ma
        else: return max(ma, sum(A)+mi)
        