""" https://leetcode.com/problems/similar-string-groups/
group similar strings using union find
"""
from header import *

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        A = list(range(n))
        def find(x):
            if A[x]!=x: A[x] = find(A[x])
            return A[x]

        def union(x, y):
            A[find(x)] = find(y)
            
        def fn(x, y): 
            cnt = 0
            for xx, yy in zip(x, y): 
                if xx != yy: cnt += 1
                if cnt > 2: return False 
            return True 
        
        for i in range(n):
            for j in range(i+1, n):
                if fn(strs[i], strs[j]):
                    union(i, j)
        return len(set([find(i) for i in range(len(A))]))