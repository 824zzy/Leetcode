""" https://leetcode.com/problems/number-of-same-end-substrings/
prefix sum + simulation
"""
from header import *


class Solution:
    def sameEndSubstringCount(
            self, s: str, queries: List[List[int]]) -> List[int]:
        pre = [0] * 26
        A = [[] for _ in range(len(s) + 1)]
        A[0] = pre.copy()

        for i, c in enumerate(s):
            pre[ord(c) - 97] += 1
            A[i + 1] = pre.copy()

        ans = []
        for i, j in queries:
            cnt = j - i + 1
            for k in range(26):
                x = A[j + 1][k] - A[i][k]
                cnt += x * (x - 1) // 2
            ans.append(cnt)
        return ans
