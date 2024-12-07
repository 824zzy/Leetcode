""" https://leetcode.com/problems/maximize-the-minimum-powered-city/
comprehensive problem: prefix sum + binary search + sweep line
"""
from header import *


class Solution:
    def maxPower(self, A: List[int], r: int, k: int) -> int:
        def check(min_power: int) -> bool:
            diff = [0] * n
            sum_d = need = 0
            for i, power in enumerate(A):
                sum_d += diff[i]
                m = min_power - power - sum_d
                if m > 0:
                    need += m
                    if need > k:
                        return True
                    # update difference
                    sum_d += m
                    if i + r * 2 + 1 < n:
                        diff[i + r * 2 + 1] -= m
            return False

        n = len(A)
        sm = list(accumulate(A, initial=0))
        for i in range(len(A)):
            A[i] = sm[min(i + r + 1, n)] - sm[max(i - r, 0)]

        left, right = min(A), min(A) + k + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1
