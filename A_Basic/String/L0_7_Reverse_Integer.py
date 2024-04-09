""" https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int) -> int:
        # check negative
        if x < 0:
            neg = True
        else:
            neg = False
        # reverse integer
        x = int(str(abs(x))[::-1])
        if neg:
            x *= -1
        # check overflow
        if x < -2**31 or x > 2**31 - 1:
            return 0
        else:
            return x
