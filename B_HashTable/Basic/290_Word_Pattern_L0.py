""" https://leetcode.com/problems/word-pattern/
the same as 205
use two hash table to check pattern and s with each other
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern)!=len(s): return False
        i2j, j2i = {}, {}
        for i, j in zip(pattern, s):
            if j not in j2i: j2i[j] = i
            if i not in i2j: i2j[i] = j
            if j2i[j]!=i or i2j[i]!=j: return False
        return True