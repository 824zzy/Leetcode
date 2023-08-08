""" https://leetcode.com/problems/sum-of-squares-of-special-elements/
simulation
"""
from header import *

class Solution:
    def sumOfSquares(self, A: List[int]) -> int:
        n = len(A)
        return sum(x*x for i, x in enumerate(A) if n%(i+1)==0)