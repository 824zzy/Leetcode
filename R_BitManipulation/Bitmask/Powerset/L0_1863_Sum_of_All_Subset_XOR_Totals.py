""" https://leetcode.com/problems/sum-of-all-subset-xor-totals/
find all subset by backtracking or power set
"""
from header import *


class Solution:
    def subsetXORSum(self, A: List[int]) -> int:
        def dfs(i, x):
            if i == len(A):
                return x
            return dfs(i+1, x)+dfs(i+1, x ^ A[i])
        return dfs(0, 0)


class Solution:
    def subsetXORSum(self, A: List[int]) -> int:
        ans = 0
        for mask in range(1 << len(A)):
            val = 0
            for i in range(len(A)):
                if mask & 1 << i:
                    val ^= A[i]
            ans += val
        return ans
