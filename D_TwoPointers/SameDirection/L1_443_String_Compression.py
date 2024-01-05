""" https://leetcode.com/problems/string-compression/
two pointers + simulation
"""
from header import *

class Solution:
    def compress(self, A: List[str]) -> int:
        A += '*'
        idx = 0
        i = 0
        for j in range(len(A)):
            if j and A[j]!=A[j-1]:
                c = A[i]
                l = j-i
                A[idx] = c
                idx += 1
                if l>1:
                    for x in str(l):
                        A[idx] = x
                        idx += 1
                i = j
        for _ in range(len(A)-idx):
            A.pop()
    
"""
["a","a","b","b","c","c","c"]
["a"]
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
["a","a","a","a","a","b"]
["#","$","#","#","$","$","$","$","#","#"]
"""