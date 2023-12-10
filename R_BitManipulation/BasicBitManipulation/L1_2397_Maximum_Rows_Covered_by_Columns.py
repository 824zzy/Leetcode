""" https://leetcode.com/problems/maximum-rows-covered-by-columns/
enumerate all possible combinations of columns, and check if the rows are covered
"""
from header import *

# bit manipulation
class Solution:
    def maximumRows(self, M: List[List[int]], n: int) -> int:
        A = []
        for i in range(len(M)):
            tmp = 0
            for j in range(len(M[0])):
                if M[i][j]:
                    tmp += 1<<j
            A.append(tmp)
        
        ans = 0
        for mask in range(1<<len(M[0])):
            if mask.bit_count()!=n:
                continue
            cnt = 0
            for x in A:
                if x&mask==x:
                    cnt += 1
            ans = max(ans, cnt)
        return ans
    
# combinatorics and array comparison
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