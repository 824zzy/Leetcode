""" https://leetcode.com/problems/movement-of-robots/
brain teaser + prefix sum
a_(i)-a_(i-1) + a_(i)-a_(i-2) + ... + a_(i)-a_(0) === i*a_(i)-(a_0+...+a_(i-1))
"""
from header import *


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10**9 + 7
        A = []
        for x, c in zip(nums, s):
            if c == 'R':
                x += d
            else:
                x -= d
            A.append(x)
        A.sort()
        ans = 0
        presum = 0
        for i, x in enumerate(A):
            ans += i * x - presum % MOD
            presum += x
        return ans % MOD

# Induction


class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        A = []
        n = len(nums)
        for x, c in zip(nums, s):
            if c == 'R':
                x += d
            else:
                x -= d
            A.append(x)
        A.sort()
        ans = 0
        f = 2 if n & 1 else 1
        for i in range(n // 2 - 1, -1, -1):
            ans += (A[~i] - A[i]) * f % (10**9 + 7)
            f += 2
        return ans % (10**9 + 7)
