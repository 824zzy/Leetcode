""" https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
similar to 921, greedily find balanced parentheses
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:
            return False
        bal = 0
        for c, l in zip(s, locked):
            if l == '0' or c == '(':
                bal += 1
            elif c == ')':
                bal -= 1
            if bal < 0:
                return False

        bal = 0
        for c, l in zip(reversed(s), reversed(locked)):
            if l == '0' or c == ')':
                bal += 1
            elif c == '(':
                bal -= 1
            if bal < 0:
                return False
        return True
