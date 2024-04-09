""" https://leetcode.com/problems/equal-row-and-column-pairs/
brute force, O(m*n)
"""
from header import *


class Solution:
    def equalPairs(self, G: List[List[int]]) -> int:
        cols = list(zip(*G))
        m, n = len(G), len(G[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if G[i] == list(cols[j]):
                    ans += 1
        return ans
