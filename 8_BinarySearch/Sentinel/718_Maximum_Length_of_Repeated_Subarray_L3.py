""" https://leetcode.com/problems/maximum-length-of-repeated-subarray/
binary search + rolling hash.

use 100*rh+A[i] as hash function
"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        
        def fn(k): 
            """Return True if a subarray of length k can be found in A and B."""
            seen = {}
            rh = 0 # rolling hash 
            for i in range(len(A)):
                rh = (100*rh + A[i] - (i >= k)*A[i-k]*100**k) % 1_000_000_007
                if i >= k-1: seen.setdefault(rh, []).append(i)
                    
            rh = 0
            for i in range(len(B)):
                rh = (100*rh + B[i] - (i >= k)*B[i-k]*100**k) % 1_000_000_007
                if i >= k-1: 
                    for ii in seen.get(rh, []): 
                        if A[ii-k+1:ii+1] == B[i-k+1:i+1]: return True 
            return False 
        
        # last True binary search 
        lo, hi = -1, len(A)
        while lo < hi: 
            mid = lo + hi + 1>> 1
            if fn(mid): lo = mid
            else: hi = mid - 1
        return lo 