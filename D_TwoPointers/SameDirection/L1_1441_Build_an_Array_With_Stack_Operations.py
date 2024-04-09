""" https://leetcode.com/problems/build-an-array-with-stack-operations/description/
linear scan and simulate the stack operations using two pointers
"""
from header import *

# simulation solution 1


class Solution:
    def buildArray(self, A: List[int], n: int) -> List[str]:
        A = [0] + A + [A[-1] + 1]
        ans = []
        for i in range(len(A) - 1):
            ans.append('Push')
            if A[i + 1] - A[i] != 1:
                ans.extend(['Push'] * (A[i + 1] - A[i] - 1) +
                           ['Pop'] * (A[i + 1] - A[i] - 1))
        return ans[1:]
