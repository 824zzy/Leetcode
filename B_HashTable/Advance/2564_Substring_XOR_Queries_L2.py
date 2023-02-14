""" https://leetcode.com/problems/substring-xor-queries/
1. Observation: val == second ^ first, and val belongs to 0 ~ 2^30-1
2. use hash table to store the first and last index of val

Time complexity: O(n^2)
"""
from header import *

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        queries = [i^j for i, j in queries]
        mp = {}
        for i in range(len(s)):
            x = 0
            for j in range(i, min(len(s), i+30)):
                x = 2*x+int(s[j])
                if x not in mp or j-i<mp[x][1]-mp[x][0]:
                    mp[x] = (i, j)
        return [mp[x] if x in mp else [-1, -1] for x in queries]