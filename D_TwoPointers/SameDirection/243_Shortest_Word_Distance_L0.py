""" https://leetcode.com/problems/shortest-word-distance/
greedily find the minimum distance between two pointers
"""
from header import *

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i, j = inf, inf
        ans = inf
        for idx, w in enumerate(wordsDict):
            if w==word1:
                i = idx
            elif w==word2:
                j = idx
            ans = min(ans, abs(i-j))
        return ans
                