""" https://leetcode.com/problems/split-the-array-to-make-coprime-products/
Think reversely: find the intervals that cannot be split, which is the leftmost and rightmost index of each prime factor
"""
from header import *


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        left = {}
        right = [0] * len(nums)

        def f(p: int, i: int) -> None:
            if p in left:
                right[left[p]] = i
            else:
                left[p] = i

        for i, x in enumerate(nums):
            d = 2
            while d * d <= x:
                if x % d == 0:
                    f(d, i)
                    x //= d
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                f(x, i)

        max_r = 0
        for l, r in enumerate(right):
            if l > max_r:
                return max_r
            max_r = max(max_r, r)
        return -1
