""" https://leetcode.com/problems/valid-word-square/
zip_longest
"""
from header import *


class Solution:
    def validWordSquare(self, A: List[str]) -> bool:
        return A == ["".join(filter(None, x)) for x in zip_longest(*A)]


"""
["abcd","bnrt","crmy","dtye"]
["abcd","bnrt","crm","dt"]
["ball","area","read","lady"]
["ball","asee","lett","le"]
"""
