""" https://leetcode.com/problems/find-missing-and-repeated-values/
simulation or use math
"""
from header import *

class Solution:
    def findMissingAndRepeatedValues(self, A: List[List[int]]) -> List[int]:
        sm = sum(sum(x) for x in A)
        seen = defaultdict(int)
        n = len(A)
        for i in range(n):
            for j in range(n):
                seen[A[i][j]] += 1
                if seen[A[i][j]]==2:
                    return [A[i][j], n*n*(n*n+1)//2+A[i][j] - sm] 
