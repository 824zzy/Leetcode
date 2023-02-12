""" https://leetcode.com/problems/substring-xor-queries/
"""
from header import *

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        queries = [i^j for i, j in queries]
        mp = {}
        for i in range(len(s)):
            if s[i]=='0': 
                mp.setdefault(0, (i, i))
                continue
            x = 0
            for j in range(i, min(len(s), i+30)):
                x = 2*x+int(s[j])
                mp.setdefault(x, (i, j))
        return [mp[x] if x in mp else [-1, -1] for x in queries]
        