""" https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
simulation using hash table
"""
from header import *

class Solution:
    def findMatrix(self, A: List[int]) -> List[List[int]]:
        cnt = Counter(A)
        ans = []
        for i, (k, v) in enumerate(sorted(cnt.items(), key=lambda x: -x[1])):
            for j in range(v):
                if i==0: ans.append([k])
                else: ans[j].append(k)
        return ans