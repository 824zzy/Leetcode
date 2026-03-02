""" https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
find the largest two numbers and return (a-1)*(b-1)
"""


class Solution:
    def maxProduct(self, A: List[int]) -> int:
        A.sort()
        return (A[-1] - 1) * (A[-2] - 1)
