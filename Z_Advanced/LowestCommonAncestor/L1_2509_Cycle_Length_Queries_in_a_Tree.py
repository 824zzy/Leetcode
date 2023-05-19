""" https://leetcode.com/problems/cycle-length-queries-in-a-tree/description/
query_length = lca(i, j) + 1
"""
from header import *

class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        for i, j in queries:
            cnt = 1
            while i!=j:
                if i>j: i //= 2
                else: j //= 2
                cnt += 1
            ans.append(cnt)
        return ans