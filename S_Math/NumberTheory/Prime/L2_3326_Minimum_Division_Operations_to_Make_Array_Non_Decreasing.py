""" https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/
LPF + greedy

1. calculate the least prime factor of each number from 2 to n
2. iterate from the end of the array, if the current number is greater than the next number, set the current number to its least prime factor
"""

from header import *

n = 10**6
LPF = [0] * n
for i in range(2, n):
    if LPF[i] == 0:
        for j in range(i, n, i):
            if LPF[j] == 0:
                LPF[j] = i


class Solution:
    def minOperations(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                A[i] = LPF[A[i]]
                if A[i] > A[i + 1]:
                    return -1
                ans += 1
        return ans


"""
[25,7]
[7,7,6]
[1,1,1,1]
"""
