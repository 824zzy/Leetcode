""" https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/
since 1 <= nums.length <= 1000, just brute force to find all valid subarrays
note that don't use array slicing, it's too slow
"""
from header import *


class Solution:
    def subarrayGCD(self, A: List[int], k: int) -> int:
        ans = 0
        for i in range(len(A)):
            x = 0
            for j in range(i, len(A)):
                x = gcd(x, A[j])
                if x == k:
                    ans += 1
        return ans
