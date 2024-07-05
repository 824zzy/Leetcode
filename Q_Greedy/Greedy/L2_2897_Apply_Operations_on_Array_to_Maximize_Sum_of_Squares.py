""" https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
observation: after any operations, the number of 1s in each bit keeps the same

greedily maximize each bit of first k numbers

Note: trick to count bits and add 2**i to ans
"""
from header import *


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        m = max(nums).bit_length()
        A = [0] * m
        for x in nums:
            for i in range(m):
                A[i] += (x >> i) & 1

        ans = 0
        for _ in range(k):
            t = 0
            for i in range(len(A)):
                if A[i]:
                    A[i] -= 1
                    t |= 1 << i
            ans = (ans + t * t) % MOD
        return ans


"""
0010
0110
0101
1000

0000
0110
0101
1010

0000
0110
0000
1111

===
0100
0101
0100
0111

0100 = 5
0101 = 5
0111 = 7

"""
