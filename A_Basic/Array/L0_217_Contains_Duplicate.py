""" https://leetcode.com/problems/contains-duplicate/
check duplicate by set
"""
from header import *

class Solution:
    def containsDuplicate(self, A: List[int]) -> bool:
        return len(set(A))!=len(A)