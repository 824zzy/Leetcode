""" https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
find numbers that are divisible by 3 and even
"""
from header import *

class Solution:
    def averageValue(self, A: List[int]) -> int:
        A = [x for x in A if x%3==0 and x%2==0] 
        return sum(A)//len(A) if A else 0