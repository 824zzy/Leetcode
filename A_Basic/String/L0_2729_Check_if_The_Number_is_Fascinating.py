""" https://leetcode.com/problems/check-if-the-number-is-fascinating/
"""


class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n) + str(2 * n) + str(3 * n)
        return "0" not in s and len(set(s)) == len(s) == 9


"""
192
100
267
783
"""
