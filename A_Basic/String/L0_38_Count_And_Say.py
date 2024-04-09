""" https://leetcode.com/problems/count-and-say/
simple usage of groupby
"""
from header import *


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            newS = ''
            for k, v in groupby(s):
                newS += str(len(list(v))) + k
            s = newS
        return s
