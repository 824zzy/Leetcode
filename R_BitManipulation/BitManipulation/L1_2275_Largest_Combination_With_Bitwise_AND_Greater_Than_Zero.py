""" https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
for each bit position, find the maximum frequency of '1'
"""

from header import *


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        A = []
        for i in range(24):
            cnt = 0
            for x in candidates:
                cnt += bool(x & 1 << i)
            A.append(cnt)
        return max(A)


# zip_longest implemntation using the same idea
class Solution:
    def largestCombination(self, A: List[int]) -> int:
        ans = 0
        for x in zip_longest(*[bin(x)[2:][::-1] for x in A]):
            ans = max(ans, x.count("1"))
        return ans
