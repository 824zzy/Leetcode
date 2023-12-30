""" https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
ensure the frequency of each character is distributable for all the words.
"""
from header import *

class Solution:
    def makeEqual(self, A: List[str]) -> bool:
        n = len(A)
        return all(v%n==0 for _, v in Counter(''.join(A)).items())