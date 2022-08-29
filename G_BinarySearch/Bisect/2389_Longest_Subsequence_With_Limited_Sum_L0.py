""" https://leetcode.com/problems/longest-subsequence-with-limited-sum/
the maximum size of a subsequence is the index of query in prefix sum array, which can be easily found by bisect
"""
from header import *

class Solution:
    def answerQueries(self, A: List[int], Q: List[int]) -> List[int]:
        A = list(accumulate(sorted(A)))
        ans = []
        for q in Q:
            ans.append(bisect_right(A, q))
        return ans