""" https://leetcode.com/problems/destination-city/
find the city that out-degree is 0
"""
from header import *

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outD = defaultdict(int)
        for i, _ in paths:
            outD[i] += 1
        for _, i in paths:
            if outD[i]==0:
                return i