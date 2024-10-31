""" https://leetcode.com/problems/find-the-maximum-factor-score-of-array/
prefix suffix decomposition + number theory

gcd(0, x) = x
lcm(1, x) = x
"""

from header import *


# prefix suffix decomposition + number theory
class Solution:
    def maxScore(self, A: List[int]) -> int:
        n = len(A)
        suf_gcd = [0] * (n + 1)
        suf_lcm = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            suf_gcd[i] = gcd(suf_gcd[i + 1], A[i])
            suf_lcm[i] = lcm(suf_lcm[i + 1], A[i])

        ans = suf_gcd[0] * suf_lcm[0]
        pre_gcd, pre_lcm = 0, 1
        for i, x in enumerate(A):
            ans = max(ans, gcd(pre_gcd, suf_gcd[i + 1]) * lcm(pre_lcm, suf_lcm[i + 1]))
            pre_gcd = gcd(pre_gcd, x)
            pre_lcm = lcm(pre_lcm, x)
        return ans


# brute force
class Solution:
    def maxScore(self, A: List[int]) -> int:
        ans = gcd(*A) * lcm(*A)
        for i in range(len(A)):
            _A = A[:i] + A[i + 1 :]
            ans = max(ans, gcd(*_A) * lcm(*_A))
        return ans
