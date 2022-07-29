""" https://leetcode.com/problems/valid-number/
advance usage of regular expression
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$", s.strip(" "))