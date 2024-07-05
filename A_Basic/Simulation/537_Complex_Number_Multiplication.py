""" L0
follow complex number multiplication rule to format string.
"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = int(num1.split("+")[0]), int(num1.split("+")[1][:-1])
        r2, i2 = int(num2.split("+")[0]), int(num2.split("+")[1][:-1])
        ans_r = r1 * r2 - i1 * i2
        ans_i = r1 * i2 + r2 * i1
        return str(ans_r) + "+" + str(ans_i) + "i"
