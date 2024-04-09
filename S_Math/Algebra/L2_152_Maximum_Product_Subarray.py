""" https://leetcode.com/problems/maximum-product-subarray/
We use prefix product which replace 0 with 1 to find maximum product.
"""


class Solution:
    def maxProduct(self, A: List[int]) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)
