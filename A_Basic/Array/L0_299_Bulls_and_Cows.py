""" https://leetcode.com/problems/bulls-and-cows/
count the number of bulls and cows
"""
from header import *

class Solution:
    def getHint(self, S: str, G: str) -> str:
        A = sum(1 for s, g in zip(S, G) if s==g)
        B = sum((Counter(S)&Counter(G)).values()) - A
        return f'{A}A{B}B'