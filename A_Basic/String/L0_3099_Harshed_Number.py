""" https://leetcode.com/problems/harshad-number/
string simulation
"""


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sm = sum(int(c) for c in str(x))
        return sm if x % sm == 0 else -1
