""" https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
Time complexity: O(2*n)
"""
class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        @cache
        def dp(i, canDel):
            if i==len(A): return -1*(canDel==1)
            
            if A[i]==1: return 1+dp(i+1, canDel)
            elif canDel: return dp(i+1, 0)
            else: return 0
        
        return max(dp(i, 1) for i in range(len(A)))