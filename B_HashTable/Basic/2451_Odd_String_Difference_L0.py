""" https://leetcode.com/problems/odd-string-difference/
transform word to difference string
"""
from header import *

class Solution:
    def oddString(self, A: List[str]) -> str:
        seen = defaultdict(list)
        for w in A:
            tmp = []
            for i in range(1, len(w)):
                tmp.append(ord(w[i])-ord(w[i-1]))
            seen[tuple(tmp)].append(w)
        
        for k, v in seen.items():
            if len(v)==1: return v[0]