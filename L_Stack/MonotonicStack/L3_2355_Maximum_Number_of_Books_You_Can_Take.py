""" https://leetcode.com/problems/maximum-number-of-books-you-can-take/
learn from guan: https://github.com/wisdompeak/LeetCode/tree/master/Stack/2355.Maximum-Number-of-Books-You-Can-Take

1. modified monotonic stack: when A[j]>A[i]-(i-j), pop j as the next smaller element on the left
2. use dp to calculate the max sum of subarray ending at i
"""
from header import *


class Solution:
    def maximumBooks(self, A: List[int]) -> int:
        L = [-1] * len(A)
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]] > A[i] - (i - stk[-1]):
                L[stk.pop()] = i
            stk.append(i)

        dp = [0] * len(A)
        for i in range(len(A)):
            if L[i] == -1:
                d = min(i + 1, A[i])
                dp[i] = (A[i] + A[i] - d + 1) * d // 2
            else:
                d = i - L[i]
                dp[i] = dp[L[i]] + (A[i] + A[i] - d + 1) * d // 2
        return max(dp)
