""" https://leetcode.com/problems/ransom-note/
use counter comparing operation
"""
from header import *
class Solution:
    def canConstruct(self, A: str, B: str) -> bool:
        return Counter(B)>=Counter(A)