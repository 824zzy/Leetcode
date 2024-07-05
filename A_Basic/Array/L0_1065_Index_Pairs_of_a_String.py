""" https://leetcode.com/problems/index-pairs-of-a-string/
brute force
"""
from header import *


class Solution:
    def indexPairs(self, A: str, words: List[str]) -> List[List[int]]:
        ans = []
        for word in words:
            for i in range(len(A) - len(word) + 1):
                if A[i : i + len(word)] == word:
                    ans.append([i, i + len(word) - 1])
        return sorted(ans)
