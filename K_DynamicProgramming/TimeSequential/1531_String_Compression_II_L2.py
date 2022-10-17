""" https://leetcode.com/problems/string-compression-ii/
idx: Index of the current symbol
lastChar: The last symbol we have in our compression
lastCharCount: The number of lastChar we have considered
k: The number of symbols we are still allowed to delete
"""
from header import *
class Solution:
    def getLengthOfOptimalCompression(self, A: str, k: int) -> int:
        @cache
        def dp(i, k, prev, cnt):
            """Return length of rle of s[i:] with k chars to be deleted."""
            if k<0: return inf
            if i==len(A): return 0
            
            is_del = dp(i+1, k-1, prev, cnt)
            if A[i]==prev:
                is_keep = dp(i+1, k, prev, cnt+1)+(cnt in [1,9,99])
            else:
                is_keep = dp(i+1, k, A[i], 1)+1
            return min(is_del, is_keep)
        
        return dp(0, k, '', 0)