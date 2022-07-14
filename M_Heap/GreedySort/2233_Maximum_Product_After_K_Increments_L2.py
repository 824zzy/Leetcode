""" https://leetcode.com/problems/maximum-product-after-k-increments/
Fill gap trick

Time complexity: O(klogn) the higher bound is less than pop k times.
"""
class Solution:
    def maximumProduct(self, A: List[int], k: int) -> int:
        heapify(A)
        n = len(A)
        while k:
            mn = heappop(A)
            if A: gap = max(k//n, 1)
            else: gap = k
            
            heappush(A, mn+gap)
            k -= gap
        
        ans = 1
        for x in A:
            ans *= x
            ans %= 10**9+7
        return ans