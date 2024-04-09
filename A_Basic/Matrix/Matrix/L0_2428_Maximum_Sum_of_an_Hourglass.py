""" https://leetcode.com/problems/maximum-sum-of-an-hourglass/
since m and n in range [3, 150], we can use brute force to solve this problem.
"""
from header import *


class Solution:
    def maxSum(self, A: List[List[int]]) -> int:
        ans = 0
        for i in range(len(A) - 2):
            for j in range(len(A[0]) - 2):
                t = A[i][j] + A[i][j + 1] + A[i][j + 2]
                m = A[i + 1][j + 1]
                b = A[i + 2][j] + A[i + 2][j + 1] + A[i + 2][j + 2]
                ans = max(ans, t + m + b)
        return ans
