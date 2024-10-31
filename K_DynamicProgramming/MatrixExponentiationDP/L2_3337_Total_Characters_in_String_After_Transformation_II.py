""" https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/
10**9 ==> log(n)
F(t) = M * F(t-1)
     = M^t * F(0)
     
dp + matrix binary exponentiation template
"""

from header import *


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            return [
                [sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
                for row in a
            ]

        def pow_mul(a: List[List[int]], n: int, f0: List[List[int]]) -> List[List[int]]:
            res = f0
            while n:
                if n & 1:
                    res = mul(a, res)
                a = mul(a, a)
                n >>= 1
            return res

        f0 = [[1] for _ in range(26)]
        M = [[0] * 26 for _ in range(26)]
        for i, c in enumerate(nums):
            for j in range(i + 1, i + c + 1):
                M[i][j % 26] = 1
        M = pow_mul(M, t, f0)

        ans = 0
        for c, cnt in Counter(s).items():
            ans += M[ord(c) - 97][0] * cnt
        return ans % MOD
