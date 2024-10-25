""" https://leetcode.com/problems/subarray-product-less-than-k/submissions/
1. compute prefix production along with sliding window
   note that restriction i<=j needs to be applied in while loop
2. ans is updated by subarray count(j-i+1)
"""

from header import *


class Solution:
    def numSubarrayProductLessThanK(self, A: List[int], k: int) -> int:
        i = 0
        prefix = 1
        ans = 0
        for j in range(len(A)):
            prefix *= A[j]
            while i <= j and prefix >= k:
                prefix /= A[i]
                i += 1
            ans += j - i + 1
        return ans
