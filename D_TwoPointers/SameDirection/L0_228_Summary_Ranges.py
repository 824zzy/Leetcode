""" https://leetcode.com/problems/summary-ranges/
construct the answer using same direction two pointers
"""
from header import *


class Solution:
    def summaryRanges(self, A: List[int]) -> List[str]:
        A += [inf]
        i = 0
        ans = []
        for j in range(1, len(A)):
            if A[j] != A[j - 1] + 1:
                if i == j - 1:
                    ans.append(str(A[i]))
                else:
                    ans.append("->".join([str(A[i]), str(A[j - 1])]))
                i = j
        return ans
