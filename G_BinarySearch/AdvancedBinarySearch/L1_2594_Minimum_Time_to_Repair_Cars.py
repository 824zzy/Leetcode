""" https://leetcode.com/problems/minimum-time-to-repair-cars/
r*n*n is monotonic increasing function ==> binary search
"""
from header import *


class Solution:
    def repairCars(self, A: List[int], cars: int) -> int:
        def fn(time):
            # return True if we can repair enough cars in time
            cnt = 0
            for x in A:
                cnt += int(sqrt(time // x))
            return cnt >= cars

        l, r = 0, min(A) * cars * cars
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l
