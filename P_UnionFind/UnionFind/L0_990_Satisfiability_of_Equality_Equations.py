""" https://leetcode.com/problems/satisfiability-of-equality-equations/
"""
from header import *


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = list(range(26))

        def find(x):
            if dsu[x] != x:
                dsu[x] = find(dsu[x])
            return dsu[x]

        def union(x, y):
            dsu[find(x)] = find(y)

        for equation in equations:
            x = ord(equation[0]) - 97
            y = ord(equation[-1]) - 97
            if equation[1:3] == "==":
                union(x, y)

        for equation in equations:
            x = ord(equation[0]) - 97
            y = ord(equation[-1]) - 97
            if equation[1:3] == "!=" and find(x) == find(y):
                return False
        return True
