""" https://leetcode.com/problems/maximum-xor-for-each-query/
"""

from header import *


class Solution:
    def getMaximumXor(self, A: List[int], maximumBit: int) -> List[int]:
        x = reduce(xor, A)
        ans = []
        mask = (1 << maximumBit) - 1
        for i in range(len(A) - 1, -1, -1):
            # k = 0
            # for j in range(maximumBit):
            #     if x&(1<<j)==0:
            #         k += (1<<j)
            ans.append(x ^ mask)
            x ^= A[i]
        return ans
