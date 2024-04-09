""" https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
use `reduce` to calculate summation and product
"""
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        A = list(map(int, str(n)))
        return reduce(lambda a, b: a * b, A) - reduce(lambda a, b: a + b, A)
