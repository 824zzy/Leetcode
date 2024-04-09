""" https://leetcode.com/problems/add-digits/
simulation
"""


class Solution:
    def addDigits(self, n: int) -> int:
        while len(str(n)) > 1:
            n = sum([int(c) for c in str(n)])
        return n
