""" https://leetcode.com/problems/string-to-integer-atoi/
take care of float and corner cases
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        A = s.lstrip().split()
        if not A:
            return 0

        x = A[0]
        op = "+"
        ans = ["0"]
        for i, c in enumerate(x):
            if i == 0 and c in "+-":
                op = c
            else:
                if c.isdigit():
                    ans.append(c)
                else:
                    break

        if op == "+":
            return min(int("".join(ans)), 2 ** 31 - 1)
        else:
            return max(-int("".join(ans)), -(2 ** 31))

        return 0
