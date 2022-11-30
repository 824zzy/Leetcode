""" https://leetcode.com/problems/unique-number-of-occurrences/
"""
from header import *

class Solution:
    def uniqueOccurrences(self, A: List[int]) -> bool:
        return len(Counter(A).values())==len(set(Counter(A).values()))