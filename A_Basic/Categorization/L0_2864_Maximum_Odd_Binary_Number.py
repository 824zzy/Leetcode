""" https://leetcode.com/problems/maximum-odd-binary-number/
two cases:
1. if there are more than 1 '1'
2. if there is only 1 '1'
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = s.count("1")
        if n > 1:
            return "1" * (n - 1) + "0" * (len(s) - n) + "1"
        else:
            return "0" * (len(s) - 1) + "1"
