""" https://leetcode.com/problems/longest-subsequence-with-limited-sum/
greedily sort + prefix sum + binary search
"""
from header import *


class Solution:
    def answerQueries(self, A: List[int], Q: List[int]) -> List[int]:
        A = list(accumulate(sorted(A)))
        ans = []
        for q in Q:
            ans.append(bisect_right(A, q))
        return ans
