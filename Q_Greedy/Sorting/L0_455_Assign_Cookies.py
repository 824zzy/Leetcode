""" https://leetcode.com/problems/assign-cookies/
1. sort two lists
2. greedily assign legit cookies to children by two pointers
"""
from header import *

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for j in range(len(s)):
            if i<len(g) and g[i]<=s[j]:
                i += 1
        return i