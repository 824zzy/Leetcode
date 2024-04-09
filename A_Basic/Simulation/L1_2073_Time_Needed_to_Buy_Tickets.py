""" https://leetcode.com/problems/time-needed-to-buy-tickets/
count minimum a and A[k] before k, and minus extra 1 after k
"""
from header import *


class Solution:
    def timeRequiredToBuy(self, A: List[int], k: int) -> int:
        for i, a in enumerate(A):
            ans += min(a, A[k] - (i > k))
        return ans

# straight forward simulation


class Solution:
    def timeRequiredToBuy(self, A: List[int], k: int) -> int:
        ans = 0
        while A[k]:
            for i in range(len(A)):
                if A[i]:
                    ans, A[i] = ans + 1, A[i] - 1
                if not A[k]:
                    break
        return ans
