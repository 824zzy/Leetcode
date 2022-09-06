""" https://leetcode.com/problems/maximum-rows-covered-by-columns/
enumerate all possible combinations of columns, and check if the rows are covered
"""
from header import *

class Solution:
    def maximumRows(self, A: List[List[int]], cols: int) -> int:
        cands = list(combinations(range(len(A[0])), cols))
        ans = 0
        for cand in cands:
            tmp = 0
            for i in range(len(A)):
                x = A[i].count(1)
                y = 0
                for j in cand:
                    if A[i][j]==1: 
                        y += 1
                if x==y: 
                    tmp += 1
            ans = max(ans, tmp)
        return ans