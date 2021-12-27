""" https://leetcode.com/problems/maximum-product-subarray/
We need to keep track of maximum and minimum prodct(product subarray) at the same time to make sure we can find global maximum.
"""
class Solution:
    def maxProduct(self, A: List[int]) -> int:
        ans, maxP, minP = -inf, 1, 1
        
        for x in A:
            maxP, minP = max(x, maxP*x, minP*x), min(x, maxP*x, minP*x)
            ans = max(ans, maxP)
        return ans